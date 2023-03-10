import unittest

def sum(a,b):
    return a+b

class SumTest(unittest.TestCase):
    def test_sum_func1(self):
        #ARRANGE
        a = 10
        b = 20
        #ACT
        result = sum(a,b)
        #ASSERT
        self.assertEqual(result, a+b)

if __name__ == "__main__":
    unittest.main()