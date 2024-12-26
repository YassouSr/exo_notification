# Notification exercise

## Folder structure

- ```tests/``` : python package contains unit tests.
- ```core/``` : python package contains main functionalities of Notification exercise, it contains the core functionalities in ```core/core.py```, necessary configurations in ```core/config.py``` and functionalities for user interaction with the console in ```core/client.py```.
- ```main.py``` : python file to run the project.

## How to execute the project

1. Install python
2. Clone the repository
3. Add your proper configuration for SMTP server in the appropriate file :

    ```py
    SMTP_CONFIG = {
        "host": "smtp.gmail.com",
        "port": 587,
        "email": "your_email@gmail.com",
        "password": "your_email_password"
    }
    ```

4. Run the project with ```python main.py```

## How to run unit tests

To execute unit tests :

```bash
# enter test folder
cd exo_notification/tests

# to run tests for core module
python -m tests.test_core

# to run tests for client module
python -m tests.test_client
```

If all tests of core module executed successfully, you'll get the following message :

```bash
Email sent successfully
Test passed: EmailNotificationAdapter sends email successfully.       
..
----------------------------------------------------------------------
Ran 2 tests in 0.003s

OK
```

If all tests of client module executed successfully, you'll get the following message :

```bash
Bye ...
.Invalid choice. Please choose either 'SMS' or 'EMAIL'.
Invalid choice. Please choose either 'SMS' or 'EMAIL'.
..Message cannot be empty. Please try again.
...
----------------------------------------------------------------------
Ran 6 tests in 0.002s

OK
```
