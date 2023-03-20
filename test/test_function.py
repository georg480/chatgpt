import unittest

from models.function import my_function


class TestMyFunction(unittest.TestCase):
    def test_output(self):
        self.assertEqual(my_function(2), 4)
        self.assertEqual(my_function(3), 9)

    def test_input(self):
        with self.assertRaises(TypeError):
            my_function("a")
