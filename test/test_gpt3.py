import unittest

from gpt3 import gpt3


class TestGPT3(unittest.TestCase):
    def test_gpt3(self):
        prompt = "This is a test prompt."
        answer, new_prompt = gpt3(prompt)

        self.assertIsInstance(answer, str)
        self.assertGreater(len(answer.strip()), 0)

        self.assertEqual(prompt + answer, new_prompt)
