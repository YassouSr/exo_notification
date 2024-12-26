import abc
from smtplib import SMTP
from .config import SMTP_CONFIG

class NotificationService(abc.ABC):
    @abc.abstractmethod
    def notify(self, message, receiver):
        pass

class SMSNotificationAdapter(NotificationService):
    def notify(self, message, receiver):
        print(f"Your message has been sent to +213{receiver} successfully")


class EmailNotificationAdapter(NotificationService):
    def notify(self, message, receiver):
        try:
            with SMTP(host=SMTP_CONFIG["host"], port=SMTP_CONFIG["port"]) as server:
                server.starttls()
                server.login(user=SMTP_CONFIG["email"], password=SMTP_CONFIG["password"])
                server.sendmail(from_addr=SMTP_CONFIG["email"], to_addrs=receiver, msg=message)

            print("Email sent successfully")
        except Exception as e:
            print("Something went wrong : " + str(e))

class NotificationFactory:
    @classmethod
    def send_notif(cls, type, message, receiver):
        match type:
            case 'sms':
                sms_channel = SMSNotificationAdapter()
                sms_channel.notify(message, receiver)
            case 'email':
                email_channel = EmailNotificationAdapter()
                email_channel.notify(message, receiver)
            case _:
                print("Not supported channel")
