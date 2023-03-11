import main
import unittest
from io import StringIO
from unittest.mock import patch


class TestMain(unittest.TestCase):
    def test_komm_chat(self):
        with patch("builtins.input", side_effect=["Hallo", "x"]):
            with patch("sys.stdout", new=StringIO()) as fake_output:
                main.komm_chat()
                self.assertEqual(
                    fake_output.getvalue().strip(),
                    "Bot: Hallo!\nBot: Was kann ich für dich tun?",
                )

    def test_erzeuge_unittest(self):
        with patch("builtins.input", return_value="test/test_script.py"):
            with patch("openai.Completion.create") as mock_create:
                mock_create.return_value = {
                    "choices": [
                        {
                            "text": "Python-Code: import unittest\n\n\nclass Test(unittest.TestCase):\n    def test_add(self):\n        self.assertEqual(add(2, 2), 4)"
                        }
                    ]
                }
                main.erzeuge_unittest("test/test_script.py", "test-model")
                with open("test/test_script_test.py", "r") as f:
                    test_file_content = f.read()
                    self.assertEqual(
                        test_file_content.strip(),
                        "import unittest\n\n\nclass Test(unittest.TestCase):\n    def test_add(self):\n        self.assertEqual(add(2, 2), 4)",
                    )

    def test_pruefe_py_gebaut(self):
        with patch("builtins.input", return_value="test/test_script.py"):
            with patch("os.system") as mock_os:
                main.pruefe_py_gebaut("test/test_script.py")
                mock_os.assert_called_once_with(
                    "python -m py_compile test/test_script.py"
                )

    def test_fragen_chat(self):
        with patch("builtins.input", return_value="Was ist Python?"):
            with patch("openai.Completion.create") as mock_create:
                mock_create.return_value = {
                    "choices": [{"text": "Python ist eine Programmiersprache."}]
                }
                antwort = main.fragen_chat()
                self.assertEqual(antwort, "Python ist eine Programmiersprache.")
