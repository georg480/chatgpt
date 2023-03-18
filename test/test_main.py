# import io
# import unittest
# from unittest.mock import patch
#
# from main import run_program
#
#
# class TestMain(unittest.TestCase):
#     @patch("builtins.input", side_effect=["u", "x"])
#     @patch("sys.stdout", new_callable=io.StringIO)
#     def test_translate_command(self, mock_stdout, mock_input):
#         run_program()
#         expected_output = "Hallo, wie geht es Ihnen?\n\nHello, how are you?\n\n"
#         self.assertEqual(mock_stdout.getvalue(), expected_output)
#
#     @patch("builtins.input", side_effect=["e", "models/dateien.py", "x"])
#     @patch("sys.stdout", new_callable=io.StringIO)
#     def test_explain_command(self, mock_stdout, mock_input):
#         run_program()
#         expected_output = "Kannst du erklären, was der Code macht und das Ergebnis als Markdown ausgeben?\n\n"
#         self.assertIn(expected_output, mock_stdout.getvalue())
