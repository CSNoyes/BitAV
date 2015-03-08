import unittest
import sys

sys.path.append("../../src")
#sys.path.append("../../src/core")

from core.util import *

class TestUtil(unittest.TestCase):  
    def setUp(self):
        self.seq = range(10)
    def test_getByteSize(self):
        iList = [1, 8, 10, 20]
        expected = [1, 1, 2, 3]
        for i, val in enumerate(iList):
            #print iList[i], expected[i]
            self.assertTrue(getByteSize(val) == expected[i])
    def test_byteArrayXor(self):
        input1 = [255, 255]
        input2 = [0, 255]
        byteArrayXor(input1, input2)
        self.assertTrue(input1[0] == 255)
        self.assertTrue(input1[1] == 0)
    def test_addAll(self):
        a = ['x']
        addAll(a, ['b','c'])
        self.assertTrue(a, ['x','b','c'])
    def test_removeAll(self):
        a = {'a':10, 'b':20, 'c':30}
        removeAll(a, ['b','c'])
        self.assertTrue(a['a'], 10)
        self.assertTrue(len(a), 1) # ['a'], 10)
        
if __name__ == "__main__":
    unittest.main(verbosity=3)