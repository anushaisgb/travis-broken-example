import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(1,2),3)

    def test_sub(self):
        self.assertEqual(calc.sub(3,2),1)

if __name__ == '__main__':
    unittest.main()
