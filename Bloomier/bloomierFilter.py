#from core.bloomierHasher import *
#import bloomierHasher
from core.bloomierHasher import BloomierHasher
from core.orderAndMatch import *
from core.orderAndMatchFinder import *
from core.utilEncode import *
from core.util import *

class BloomierFilter:
    def __init__(self, hashSeed, keysDict, m, k, q, useTable = False):
        self.hashSeed = hashSeed
        self.keysDict = keysDict
        self.m = m
        self.k = k
        self.q = q
        self.hasher = BloomierHasher(hashSeed, m, k, q)
        self.byteSize = getByteSize(q)
        
        oamf = OrderAndMatchFinder(hashSeed, keysDict, m, k, q)
        oam =  oamf.find()
        
        ## TODO - this can be just bytearray 
        self.table = [[0] * self.byteSize] * m
        self.valueTable = [0] * m

        if useTable is False:
            self.create(keysDict, oam)
        
    def getTable(self): return self.table
    def setTable(self, table): self.table = table
    def getValueTable(self): return self.valueTable
    def setValueTable(self, table): self.valueTable = table
        
    def xorOperations(self, value, M, neighbors):
        #value = [0] * self.byteSize
        #print "???", value
        byteArrayXor(value, M)
        
        for v in neighbors:
            byteArrayXor(value, self.table[v])
        
        return value
        
    def get(self, key):
        neighbors = self.hasher.getNeighborhood(key)
        mask = self.hasher.getM(key)
        
        #print neighbors
        valueToGet = [0] * self.byteSize
        self.xorOperations(valueToGet, mask, neighbors)
        
        h = decode(valueToGet) # , self.byteSize)
        
        try:
            L = neighbors[h]
            return self.valueTable[L]
        except IndexError:
            return None
            
    def set(self, key, value):
        neighbors = self.hasher.getNeighborhood(key)
        mask = self.hasher.getM(key)
        
        #print neighbors
        valueToGet = [0] * self.byteSize
        self.xorOperations(valueToGet, mask, neighbors)
        
        h = decode(valueToGet) # , self.byteSize)
        
        try:
            L = neighbors[h]
            self.valueTable[L] = value
            return True
        except IndexError:
            return False    
            
    def create(self, map, oam):
        assert (oam is not None)
        piList = oam.piList
        tauList = oam.tauList
        #print pi, tau
        
        for i, pi in enumerate(piList):
        #for pi in piList:
            key = pi
            value = map[key]
            #print value
            neighbors = self.hasher.getNeighborhood(key)
            mask = self.hasher.getM(key)
            l = tauList[i] # tauList contains the iota values
            L = neighbors[l]
            
            encodeValue = encode(l, self.byteSize)
            valueToStore = [0] * self.byteSize
            
            byteArrayXor(valueToStore, encodeValue)
            byteArrayXor(valueToStore, mask)
            
            for i, v in enumerate(neighbors):
                if i == l:
                    pass
                else:
                    # The h_value in the table should be applied
                    byteArrayXor(valueToStore, self.table[v])

            self.table[L] = valueToStore
            self.valueTable[L] = value
        #print self.valueTable
        
    def table2string(self):
        """
        transforms table into byte array
        """
        #self.table = [[0] * self.byteSize] * m
        #self.valueTable = [0] * m
        result = chr(self.byteSize) + int2string(self.m) + chr(4) # header are 6 bytes (5 bytes + 1 for the valueTable width)
        #                                                      ^ <-- Wwe use 4 byte for value storage
        for row in self.table:
            #print row
            temp = byteArray2string(row)
            #sprint(temp)
            result += temp

        #print len(result)
        #result = int2string(len(result)) + result
        for row in self.valueTable:
            #print(row)
            result += int2string(row, 4) # or int2string(row, 2) to store 2 bytes only

        return result
        
    def string2table(self, string):
        assert type(string) is str
        # 9 bytes of header should be analyzed
        startOfData = 6
        byteSize = ord(string[0])
        m = string2int(string[1:5])
        valueSize = string2int(string[5:startOfData])

        lengthOfFirstTable = m * byteSize

        firstTable = string[startOfData:startOfData + lengthOfFirstTable]
        valueTable = string[startOfData + lengthOfFirstTable:]

        t1 = []
        t2 = []
        for i in range(m):
            # firstTable[i*byteSize:(i+1)*byteSize] returns array of chars ['\x01'...]
            temp1 = [ord(x) for x in firstTable[i*byteSize:(i+1)*byteSize]]
            t1.append(temp1)
            #print len(valueTable[i*valueSize:(i+1)*valueSize])
            temp2 = string2int(valueTable[i*valueSize:(i+1)*valueSize])
            t2.append(temp2)
        # setup the table now
        return t1, t2
        
if __name__ == "__main__":
    sys.path.append("../test")
    from testBloomierFilter import *
    
    unittest.main(verbosity=2)