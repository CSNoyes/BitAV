import unittest
import sys
import zlib
sys.path.append("../src")

FILTER_TEST = True
FILTER_SIZE_TEST = True

from bloomierFilter import *

class TestBloomierFilter(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_simple(self):
        k = {"abc":10, "def":20, "abd":30}
        bf = BloomierFilter(0, k, 10, 3, 8)

        #print "****\n\n\n"
        self.assertEqual(bf.get("abd"), k["abd"])
        self.assertEqual(bf.get("abc"), k["abc"])
        self.assertEqual(bf.get("def"), k["def"])
        self.assertEqual(bf.get("xyz"), None)
        
        bf.set("def", 12)
        self.assertEqual(bf.get("def"), 12)
        
        # return the value back
        bf.set("def", k["def"])
        return bf
        
    def atest_givenTable(self):
        bfGiven = self.test_simple()
        table = bfGiven.getTable()
        valueTable = bfGiven.getValueTable()
        
        k = {"abc":10, "def":20, "abd":30}
        bf = BloomierFilter(0, k, 10, 3, 16, useTable=True)
        bf.setTable(table)
        bf.setValueTable(valueTable)
        
        self.assertEqual(bf.get("abd"), k["abd"])
        self.assertEqual(bf.get("abc"), k["abc"])
        self.assertEqual(bf.get("def"), k["def"])
        self.assertEqual(bf.get("xyz"), None)
        
        bf.set("def", 12)
        self.assertEqual(bf.get("def"), 12)
        
    def test_bigTable(self):
        # hashSeed, keysDict, m, k, q
        # m should be multiple of the size m
        # k 
        # q : bit size 
        
        k = {}
        for i in range(1000):
            k[str(i)] = i
            
        m = int(len(k)*1.5) # len(k) * 1.1
            
        bf = BloomierFilter(0, k, m, 5, 16)
        for i in range(1000):
            self.assertEqual(bf.get(str(i)), i)
            
            
        if FILTER_SIZE_TEST:
            res = bf.table2string()
        
            print '\nbloomier'
            print len(res)
            #sprint(zlib.compress(res))
            print len(zlib.compress(res))
        
            print '\narray'
            res = map2string(k)
            print len(res)
            #sprint(zlib.compress(res))
            print len(zlib.compress(res))

        if FILTER_TEST:
            #false positive
            falsePositive = 0
            for i in range(1000, 20000):
                #print bf.get(str(i))
                if bf.get(str(i)) is not None:
                    falsePositive += 1
            print >> sys.stderr, "# of False positive %d: %f%%" % (falsePositive, 100.0*falsePositive/(20000 - 1000))
        
    
    def test_table2string(self):
        k = {"abc":10, "def":20, "abd":30}
        bf = BloomierFilter(0, k, 10, 3, 16)
        res = bf.table2string()
        self.assertEqual(66, len(res))
        return res
        
        if FILTER_SIZE_TEST:
            #sprint(res)
            print '\nbloomier'
            print len(res)
            #sprint(zlib.compress(res))
            print len(zlib.compress(res))
        
            print '\narray'
            res = map2string(k)
            print len(res)
            #sprint(zlib.compress(res))
            print len(zlib.compress(res))
            
    def test_string2table(self):
        k = {"abc":10, "def":20, "abd":30}
        bf = BloomierFilter(0, k, 10, 3, 16) # m = 10, k = 3, q = 16 (2 bytes)
        originalTable1 = bf.getTable()
        originalTable2 = bf.getValueTable()
        res = self.test_table2string()
        table1, table2 = bf.string2table(res)
        self.assertEqual(table1, originalTable1)
        self.assertEqual(table2, originalTable2)


if __name__ == "__main__":
    unittest.main(verbosity=2)