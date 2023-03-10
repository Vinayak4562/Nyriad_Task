import unittest

def sum(a,b):
    return a+b

class SumTest(unittest.TestCase):
    def setUp(self):
       print("Set up is called.....!")
        #ARRANGE
       self.a = 10
       self.b = 20

    def test_sum_func1(self):
        print("function 1 is called.....!")
        #ACT
        result = sum(self.a,self.b)
        #ASSERT
        self.assertEqual(result, self.a + self.b)
    
    def test_sum_func2(self):
        print("function 2 is called.....!")
       
        #ACT
        result = sum(self.b,self.a)
        #ASSERT
        self.assertEqual(result, self.a + self.b)

if __name__ == "__main__":
    unittest.main()


""" OutPut:

Set up is called.....!
function 1 is called.....!
.Set up is called.....!
function 2 is called.....!
.
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK 

"""