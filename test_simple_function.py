import unittest
from simple_function import greet

class TestSimpleFunction(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("Bob"), "Hello, Bob!")
        self.assertEqual(greet(""), "Hello, !")

if __name__ == "__main__":
    unittest.main()
