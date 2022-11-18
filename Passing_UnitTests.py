#!/usr/bin/python3
# Test case for performing fibonacci
import unittest

from fibonacci_function import fibonacci

class TestCase(unittest.TestCase):

    def testcase1_pass(self):
        #testcase which should pass
        test = 1
        result = fibonacci(test)
        self.assertEqual(result, 1)
    
    def testcase2_pass(self):
        #testcase which should pass
        test = 6
        result = fibonacci(test)
        self.assertEqual(result, 8)
    
    def testcase3_pass(self):
        #testcase which should pass
        test = 12
        result = fibonacci(test)
        self.assertEqual(result, 144)

    
if __name__ == '__main__':
    unittest.main()
