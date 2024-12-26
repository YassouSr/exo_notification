from unittest import TestCase, main
from unittest.mock import patch # to mock objs during tests 
from core.client import is_exit_choice, get_channel, get_message

class TestClientFunctions(TestCase):
    # test parameter of function only
    def test_is_exit_choice(self):
        self.assertTrue(is_exit_choice("exit"))
        self.assertFalse(is_exit_choice("sms"))
        self.assertFalse(is_exit_choice(""))

    # test the user input which requires mocking (simulate user input)
    @patch('builtins.input', side_effect=["sms", "email"])
    def test_get_channel_valid(self, mock_input):
        self.assertEqual(get_channel(), "sms")
        self.assertEqual(get_channel(), "email")
    
    @patch('builtins.input', side_effect=["exit"])
    def test_get_channel_exit(self, mock_input):
        with self.assertRaises(SystemExit):
            get_channel()
    
    @patch('builtins.input', side_effect=["invalid", "bla", "email"])
    def test_get_channel_invalid(self, mock_input):
        self.assertEqual(get_channel(), "email")
    
    @patch('builtins.input', side_effect=["", "here is a message"])
    def test_get_message_invalid(self, mock_input):
        self.assertEqual(get_message(), "here is a message")

    @patch('builtins.input', side_effect=["here is a message"])
    def test_get_message_valid(self, mock_input):
        self.assertEqual(get_message(), "here is a message")

if __name__ == '__main__':
    main() 
