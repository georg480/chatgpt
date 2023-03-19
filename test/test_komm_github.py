import os.path
import subprocess
import unittest

import komm_github


class TestGitCommit(unittest.TestCase):
    def test_git_commit(self):
        print(os.getcwd())
        os.remove("commit_template.txt")
        komm_github.git_commit()

        self.assertTrue(os.path.isfile("commit_template.txt"))

        with open("commit_template.txt", "r", encoding="utf-8", newline="\n") as f:
            template = f.read()
            expected_template = "- commit_template.txt\n\n- test/test_komm_github.py\n\nFunktion hinzufügen."
            self.assertEqual(template.strip(), expected_template)

        subprocess.call(["git", "reset", "--hard"])
        subprocess.call(["git", "clean", "-f"])
        os.remove("commit_template.txt")
