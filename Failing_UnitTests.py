#!/usr/bin/python3

import unittest

from fibonacci_function import fibonacci
#hello_world
class TestCase(unittest.TestCase):
    def testcase1_fail(self):
    
        test = -2
        result = fibonacci(test)
        self.assertEqual(result, 500)
    
    def testcase2_fail(self):
       
        test = 1.5
        result = fibonacci(test)
        self.assertEqual(result, 1000)

if __name__ == '__main__':
    unittest.main()
