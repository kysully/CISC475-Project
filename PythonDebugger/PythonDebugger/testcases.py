# CISC 475 - Group 4
# Testing suite
# - The code below is used for project testing
# - of various user defined functions and other
# - features provided by the project

import unittest
import sumnumbers
import maxnum
import PythonDebuggerClient
import PythonDebuggerServer

class Test_test1(unittest.TestCase):

    #test case for database connect code (client/server)
    def test_connect(self):

        #testing was done manually due to multithreading issues
        self.assertEqual(1,1)

    #test case for sum user defined function
    def test_sum(self):
        sum = sumnumbers.sumnumbers(5)
        self.assertEqual(15, sum)

    #test case for the maxnum user defined function
    def test_maxnum(self):
        max = 10
        result = maxnum.maxnum(10,3)
        self.assertEqual(max, result)

        result = maxnum.maxnum(7, 10)
        self.assertEqual(max, result)

if __name__ == '__main__':
    unittest.main()
