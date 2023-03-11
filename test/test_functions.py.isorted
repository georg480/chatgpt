import os
import subprocess
import unittest
from unittest.mock import patch

from models.functions import pruefe_py_gebaut


class TestFunctions(unittest.TestCase):
    @patch("subprocess.call")
    def test_pruefe_py_gebaut(self, mock_subprocess_call):
        skript_name = "main.py"
        with patch.object(
            os,
            "getcwd",
            return_value=r"C:\Users\georg\Seafile\Meine Bibliothek-008100\Dokumente\documents\programmieren\PycharmProjects\chatgpt",
        ):
            pruefe_py_gebaut(skript_name)

        mock_subprocess_call.assert_any_call("isort .", shell=True)
        mock_subprocess_call.assert_any_call("black .", shell=True)
        mock_subprocess_call.assert_any_call("pylint " + skript_name, shell=True)
        mock_subprocess_call.assert_any_call(
            "pyreverse -a1 -s1  -f ALL -d ALL  .  -o pdf", shell=True
        )
        mock_subprocess_call.assert_any_call("pytest", shell=True)
