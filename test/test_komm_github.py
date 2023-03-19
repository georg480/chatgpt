import os.path
import subprocess
import unittest

import komm_github


class TestGitCommit(unittest.TestCase):
    def test_git_commit(self):
        # Ausführung der Funktion
        komm_github.git_commit()

        # Überprüfung, ob die Commit-Template-Datei erstellt wurde
        self.assertTrue(os.path.isfile("commit_template.txt"))

        # Überprüfung des Inhalts der Commit-Template-Datei
        with open("commit_template.txt", "r", encoding="utf-8") as f:
            template = f.read()
            expected_template = "- komm_github.py\n\nFunktion hinzufügen."
            self.assertEqual(template.strip(), expected_template)

        # Bereinigung der Testumgebung
        subprocess.call(["git", "reset", "--hard"])
        subprocess.call(["git", "clean", "-f"])
        os.remove("commit_template.txt")
