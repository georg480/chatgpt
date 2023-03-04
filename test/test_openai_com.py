import unittest
from unittest.mock import patch
import openai_com

class TestOpenAICom(unittest.TestCase):

    @patch("openai_com.randint")
    def test_play_random_greater(self, mock_randint):
        mock_randint.return_value = 8
        expected_response = "größer"
        actual_response = openai_com.play_random()
        self.assertEqual(actual_response, expected_response)

    @patch("openai_com.randint")
    def test_play_random_smaller(self, mock_randint):
        mock_randint.return_value = 3
        expected_response = "kleiner"
        actual_response = openai_com.play_random()
        self.assertEqual(actual_response, expected_response)

