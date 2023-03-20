import unittest
from unittest.mock import call, patch

from models.functions import eingabe, pruefe_py_gebaut


class TestFunctions(unittest.TestCase):
    @patch("subprocess.call")
    def test_pruefe_py_gebaut(self, mock_subprocess_call):
        skript_name = "test_script.py"
        pruefe_py_gebaut(skript_name)
        expected_calls = [
            call("isort .", shell=True),
            call("black .", shell=True),
            call("pylint " + skript_name, shell=True),
            call("pytest", shell=True),
        ]
        mock_subprocess_call.assert_has_calls(expected_calls)

    @patch("builtins.input", return_value="Testeingabe")
    def test_eingabe(self, mock_input):
        anzeige = "Bitte geben Sie etwas ein: "
        output = eingabe(anzeige)
        mock_input.assert_called_once_with(anzeige)
        self.assertEqual(output, "Testeingabe")

    @patch("builtins.input", side_effect=["", "Testeingabe"])
    def test_eingabe_leer(self, mock_input):
        anzeige = "Bitte geben Sie etwas ein: "
        output = eingabe(anzeige)
        expected_calls = [
            call(anzeige),
            call("Die Eingabe darf nicht leer sein!"),
            call(anzeige),
        ]
        mock_input.assert_has_calls(expected_calls)
        self.assertEqual(output, "Testeingabe")
