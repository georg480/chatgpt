import os
from unittest import TestCase, mock

import openai
from dotenv import load_dotenv

load_dotenv()
from openai_com import erzeuge_unittest


class TestOpenAI(TestCase):
    @mock.patch("openai.Completion.create")
    def test_erzeuge_unittest(self, mock_create):
        mock_create.return_value.choices[0].text = (
            "import unittest\n\nclass TestMyClass(TestCase):\n"
            "    def test_my_function(self):\n"
            "        self.assertEqual(1 + 1, 2)\n"
        )
        openai.api_key = os.getenv("OPENAI_API_KEY")

        skript_quelle = "komm_unittest.py"
        model = "text-davinci-003"

        erzeuge_unittest(skript_quelle, model)

        expected_content = (
            "import unittest\n\nclass TestMyClass(TestCase):\n"
            "    def test_my_function(self):\n"
            "        self.assertEqual(1 + 1, 2)\n"
        )

        with open(f"test/test_{skript_quelle}.py", "r") as f:
            actual_content = f.read()

        os.remove(f"test/test_{skript_quelle}.py")

        self.assertEqual(actual_content, expected_content)
