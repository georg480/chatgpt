import os
import unittest
from unittest.mock import patch

from openai_com import erzeuge_unittest


class TestOpenAI(unittest.TestCase):
    @patch("openai.Completion.create")
    @patch("openai_com.chat")
    @patch("openai_com.schreibe_protokol")
    def test_erzeuge_unittest(self, mock_schreibe_protokol, mock_chat, mock_completion_create):
        mock_chat.return_value = "Python-Code: def add(a, b):\n    return a + b\n"
        mock_response = {"choices": [{"text": "Python-Code: import unittest\n\ndef test_add():\n    assert add(1, 2) == 3\n"}]}
        mock_completion_create.return_value = mock_response

        skript_quelle = "main.py"
        model = "text-davinci-002"

        erzeuge_unittest(skript_quelle, model)

        mock_chat.assert_called_with("Schreibe zu der Funktion einen Unittest der in einem extra Datei ist.\n\n==== Python-Code ====\n\nPython-Code:\n['import os\\n', 'import sys\\n', 'from typing import List\\n', '\\n', 'def add(a: int, b: int) -> int:\\n', '    return a + b\\n']")
        mock_completion_create.assert_called_with(
            model=model,
            prompt="Schreibe zu der Funktion einen Unittest der in einem extra Datei ist.\n\n==== Python-Code ====\n\nPython-Code:\n['import os\\n', 'import sys\\n', 'from typing import List\\n', '\\n', 'def add(a: int, b: int) -> int:\\n', '    return a + b\\n']",
            temperature=0.9,
            max_tokens=2150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
        )

        with open("test/test_functions.py", "r") as f:
            test_file_content = f.read()
            self.assertEqual(test_file_content.strip(), "import unittest\ndef test_add():\n    assert add(1, 2) == 3")
