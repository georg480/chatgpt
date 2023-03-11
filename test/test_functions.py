import unittest
import subprocess
import os
from unittest.mock import patch
from models.functions import pruefe_py_gebaut

class TestFunctions(unittest.TestCase):

    @patch('subprocess.call')
    def test_pruefe_py_gebaut(self, mock_subprocess_call):
        skript_name = "test_script.py"
        with patch('models.functions.os') as mock_os:
            mock_os.getcwd.return_value = '/path/to/test/directory'
            pruefe_py_gebaut(skript_name)

        mock_subprocess_call.assert_called_with("isort .", shell=True)
        mock_subprocess_call.assert_called_with("black .", shell=True)
        mock_subprocess_call.assert_called_with("pylint " + skript_name, shell=True)
        mock_subprocess_call.assert_called_with("pyreverse -a1 -s1  -f ALL -d ALL  .  -o pdf", shell=True)
        mock_subprocess_call.assert_called_with("pytest", shell=True)
