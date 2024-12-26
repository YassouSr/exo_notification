from unittest import TestCase, main
from unittest.mock import patch, MagicMock
from core.core import EmailNotificationAdapter, NotificationFactory
from core.config import SMTP_CONFIG

class TestEmailNotificationAdapter(TestCase):
    @patch('core.core.SMTP')
    def test_notify_success(self, mock_smtp):
        # Arrange
        mock_server = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_server
        adapter = EmailNotificationAdapter()
        message = "Test email message"
        receiver = "receiver@example.com"

        # Act
        adapter.notify(message, receiver)

        # Assert
        mock_smtp.assert_called_once_with(host=SMTP_CONFIG["host"], port=SMTP_CONFIG["port"])
        mock_server.starttls.assert_called_once()
        mock_server.login.assert_called_once_with(user=SMTP_CONFIG["email"], password=SMTP_CONFIG["password"])
        mock_server.sendmail.assert_called_once_with(
            from_addr=SMTP_CONFIG["email"],
            to_addrs=receiver,
            msg=message
        )
        print("Test passed: EmailNotificationAdapter sends email successfully.")

class TestNotificationFactory(TestCase):
    @patch("core.core.SMSNotificationAdapter.notify")
    @patch("core.core.EmailNotificationAdapter.notify")
    def test_send_notif(self, mock_email_notify, mock_sms_notify):
        factory = NotificationFactory()
        
        factory.send_notif('sms', "Test SMS", "123456789")
        mock_sms_notify.assert_called_with("Test SMS", "123456789")
        
        factory.send_notif('email', "Test Email", "test@example.com")
        mock_email_notify.assert_called_with("Test Email", "test@example.com")
    
if __name__ == '__main__':
    main()
