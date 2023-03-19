import os.path
import subprocess
import unittest
import sys
print(os.getcwd())
import komm_github


class TestGitCommit(unittest.TestCase):
    def test_git_commit(self):
        komm_github.git_commit()
        print(os.getcwd())
        datei_name="commit_template.txt"

        self.assertTrue(os.path.isfile(datei_name))
        #
        with open(datei_name, "r", encoding="utf-8", newline="\n") as file:
              template = file.read()
              expected_template =('- __pycache__/test_komm_github.cpython-311-pytest-7.2.1.pyc\r\n'
                                  '- test_komm_github.py\r\n'
                                  '- ../main.py\r\n'
                                  '- ../models/namensmodel.py\r\n'
                                  '\r\n'
                                  'Funktion hinzufügen.')

              #"- "+datei_name+"\n\n- test/test_komm_github.py\n\nFunktion hinzufügen."
              self.assertEqual(template.strip(), expected_template)

        # subprocess.call(["git", "reset", "--hard"])
        # subprocess.call(["git", "clean", "-f"])
      #  os.remove(datei_name)
