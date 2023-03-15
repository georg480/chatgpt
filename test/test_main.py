import unittest

from komm_revchatgpt import chat


class TestKommRevchatGPT(unittest.TestCase):
    def test_chat(self):
        model = "davinci"
        question = "What is the capital of Germany?"
        response = chat(question, model, 2035)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, str)
        self.assertNotEqual(response, "")


if __name__ == "__main__":
    unittest.main()
