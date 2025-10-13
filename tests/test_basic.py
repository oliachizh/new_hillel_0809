import unittest
import sys
import pathlib
print(pathlib.Path(__file__).parent.parent)
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from functions import factorial

class FactorialTests(unittest.TestCase):
    def test_type_error_on_non_int(self):
        with self.assertRaises(TypeError):
            factorial('5')

    def test_factorial2(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)

# class MyTestCase(unittest.TestCase):
#     def test_assert(self):
#         actul = 1
#         expected = 1
#         self.assertEqual(actul, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)