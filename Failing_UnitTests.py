#!/usr/bin/python3

import unittest

from fibonacci_function import fibonacci

class TestCase(unittest.TestCase):
    def testcase1(self):
    
        test = -2
        result = fibonacci(test)
        self.assertEqual(result, 500)
    
    def testcase2(self):
       
        test = 1.5
        result = fibonacci(test)
        self.assertEqual(result, 1000)

if __name__ == '__main__':
    unittest.main()
