from core.core import NotificationFactory
from core.client import get_channel, get_message, get_receiver, get_input, is_exit_choice

while True:
    channel = get_channel()
    message = get_message()
    receiver = get_receiver(channel)

    # Sending the notification
    factory = NotificationFactory()
    factory.send_notif(channel, message, receiver)

    # Continue or exit prompt
    next_action = get_input("Type anything to continue or type EXIT to exit: ").lower()
    if is_exit_choice(next_action):
        print("Bye ...")
        break
