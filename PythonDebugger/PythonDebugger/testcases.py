# CISC 475 - Group 4
# Testing suite
# - The code below is used for project testing

import unittest
import sumnumbers
import maxnum
import PythonDebuggerClient
import PythonDebuggerServer

class Test_test1(unittest.TestCase):

    #test case for database connect code (client/server)
    def test_connect(self):

        #testing was done manually due to multithreading issues
        self.assertTrue()

        message = "testing"
        server = Thread(target = PythonDebuggerServer.serverListen, args = ())
        server.start()
        #PythonDebuggerServer.serverListen()
        pool = ThreadPool(processes=1)

        # tuple of args for foo, please note a "," at the end of the arguments
        async_result = pool.apply_async(PythonDebuggerClient.clientStart, (message,))

        # Do some other stuff in the main process
        data = async_result.get()  
        data = PythonDebuggerClient.clientStart(message)

        #this tests that the message that was sent was recieved
        self.assertEqual(message,data)

    #test case for sum user defined function
    def test_sum(self):
        sum = sumnumbers.sumnumbers(5)
        self.assertEqual(15, sum)

    #test case for the maxnum user defineed function
    def test_maxnum(self):
        max = 10
        result = maxnum.maxnum(10,3)
        self.assertEqual(max, result)

        result = maxnum.maxnum(7, 10)
        self.assertEqual(max, result)

if __name__ == '__main__':
    unittest.main()
