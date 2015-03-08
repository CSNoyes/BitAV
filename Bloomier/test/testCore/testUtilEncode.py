import unittest
import sys

sys.path.append("../../src")
#sys.path.append("../../src/core")

from core.utilEncode import *

class TestUtilEncode(unittest.TestCase):  
    def setUp(self):
        pass
        
    def atest_encodeWidth4(self):
        res = encode(1234331245, 4)
        self.assertEqual([73, 146, 102, 109], res)
        return res
        
    def atest_decodeWidth4(self):
        res = self.test_encodeWidth4()
        self.assertEqual(1234331245, decode(res))
        
    def test_encodeWidth2(self):
        data = 43*256 + 10
        res = encode(data, 2)
        self.assertEqual([43, 10], res)
        return res, data

    def test_decodeWidth2(self):
        res, data = self.test_encodeWidth2()
        self.assertEqual(data, decode(res))
    
    def atest_encodeWidth1(self):
        data = 43
        res = encode(data, 1)
        self.assertEqual([data], res)
        return res, data

    def atest_decodeWidth1(self):
        res, data = self.test_encodeWidth1()
        self.assertEqual(data, decode(res))
        
if __name__ == "__main__":
    unittest.main(verbosity=3)