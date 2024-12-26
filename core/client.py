VALID_CHANNELS = {"sms", "email"}

def get_input(prompt):
    return input(prompt).strip().lower()


def is_exit_choice(user_input):
    return user_input == "exit"


def get_channel():
    while True:
        channel = get_input("Please choose SMS or EMAIL notifications, or type EXIT to exit : ")
        
        if is_exit_choice(channel):
            print("Bye ...")
            exit()

        if channel in VALID_CHANNELS:
            return channel
        
        print("Invalid choice. Please choose either 'SMS' or 'EMAIL'.")


def get_message():
    while True:
        message = get_input("Type the message you want to send : ")

        if message:
            return message
        
        print("Message cannot be empty. Please try again.")


def get_receiver(channel):
    prompt = "Type the phone number to send your message to : " if channel == "sms" else "Type the email to send your message to : "

    while True:
        receiver = get_input(prompt)

        if receiver:
            return receiver
        
        print(f"{'Phone number' if channel == 'sms' else 'Email'} cannot be empty. Please try again.")
