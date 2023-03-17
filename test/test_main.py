import os
import unittest

from komm_revchatgpt import erzeuge_unittest


class TestErzeugeUnittest(unittest.TestCase):
    def setUp(self):
        self.script_name = "test_skript.py"
        self.model = "davinci"
        self.dateiname = "test_unittest.py"
        erzeuge_unittest(self.script_name, self.model, self.dateiname)

    def test_unittest(self):
        # Check if the generated file exists
        self.assertTrue(os.path.exists(self.dateiname))

        # Execute the generated test file
        with open(self.dateiname) as f:
            code = compile(f.read(), self.dateiname, "exec")
            exec(code, globals(), locals())

        # Test the function that was tested in the generated file
        self.assertEqual(hello_world(), "Hello, World!")

    def tearDown(self):
        os.remove(self.dateiname)


# Function that will be tested in the generated test file
def hello_world():
    return "Hello, World!"
