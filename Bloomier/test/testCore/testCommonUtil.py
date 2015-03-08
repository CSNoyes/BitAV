import unittest
import sys

sys.path.append("../../src")
#sys.path.append("../../src/core")

from core.commonUtil import *

class TestCommonUtil(unittest.TestCase):  
    def setUp(self):
        self.testString = '\x01\x02\x03\x04'
        self.testArray = [1,2,3,4]
        self.testinteger = 123456
        
    def test_sprint(self):
        string = self.testString
        res = sprint(string, 'digit', silent=True)
        self.assertTrue('[1][2][3][4]' == res)
        
        string = '\xFF\xF1\xF2\xF3'
        res = sprint(string, 'hex', silent=True)
        self.assertTrue('[0xff][0xf1][0xf2][0xf3]' == res)
        
    def test_string2byteArray(self):
        res  = string2byteArray(self.testString)
        self.assertEqual(res, self.testArray)
        
    def test_byteArray2string(self):
        value = [1,2,3,4]
        res = byteArray2string(value)
        self.assertEqual(res, '\x01\x02\x03\x04')
    
    def test_int2byteArray(self):
        res = int2byteArray(self.testinteger) # [0, 1, 226, 64]
        self.assertEqual(res, [0,1,226,64])
        return res
        
    def test_byteArray2int(self):
        res = self.test_int2byteArray()
        self.assertEqual(self.testinteger, byteArray2int(res))
        
    def test_int2string(self):
        res = int2string(self.testinteger)
        self.assertEqual('\x00\x01\xe2\x40', res)
        
    def test_int2string2Byte(self):
        res = int2string(10*256 + 10, 2)
        self.assertEqual(res, '\x0a\x0a')
        
    def test_map2string(self):
        map = {'abc':10, 'def':20, 'xyz':40}
        res = map2string(map)
        #sprint(res)
        #print len(res)
        self.assertEqual(33, len(res))
        return res
        
    def test_string2int(self):
        self.assertEqual(123456, string2int('\x00\x01\xe2\x40'))
        
    def test_string2map(self):
        res = self.test_map2string()
        m = string2map(res)
        self.assertTrue(m['abc'] == 10)
        self.assertTrue(m['def'] == 20)
        self.assertTrue(m['xyz'] == 40)
        
if __name__ == "__main__":
    #pass
    unittest.main(verbosity=3)