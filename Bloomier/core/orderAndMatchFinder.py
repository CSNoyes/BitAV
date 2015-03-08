from bloomierHasher import *
from orderAndMatch import *
from copy import *
from singletonFindingTweaker import *
from util import *
import sys

class OrderAndMatchFinder:
    # def __init__(self, hashSeed, keysDict, m, k, q, maxTry = 5)
    # removes the maxTry is None part code ???
    ## This code is very wrong! 
    def __init__(self, hashSeed, keysDict, m, k, q, maxTry = 5):
        self.hashSeed = hashSeed
        self.keysDict = keysDict
        self.m = m
        self.k = k
        self.q = q
        self.maxTry = maxTry
        # if maxTry is None:
        #     self.maxTry = 5
        # else:
        #     self.maxTry = maxTry
        
        # the list length should be len(keysDict)
        self.piList = []
        self.tauList = []
        #self.oam = OrderAndMatch(self.piList, self.tauList)
        #self.hasher = BloomierHasher(hashSeed, m, k, q)
        
    def findMatch(self, remainingKeysDict, bloomierHasher):
        if not remainingKeysDict: return True
        #if len(remainingKeysDict) == 0: return True
        piTemp = []
        tauTemp = []
        
        tweaker = SingletonFindingTweaker(remainingKeysDict, bloomierHasher)
        #print tweaker
        
        for key in remainingKeysDict:
            # smchoPrint
            #print key + str(tweaker.getNeighborhood(key)) + "\n"
            res = tweaker.tweak(key)
            if res is not None:
                tauTemp.append(res)
                piTemp.append(key)
        # smchoPrint
        # print tauTemp
        # print piTemp
                
        if len(piTemp) == 0:
            return False
        
        removeAll(remainingKeysDict, piTemp)
        
        # len(X) != 0 is expensive, use if X: instead 
        if remainingKeysDict:
        #if len(remainingKeysDict) != 0:
            if self.findMatch(remainingKeysDict, bloomierHasher) == False:
                return False    
        
        addAll(self.piList, piTemp)
        addAll(self.tauList, tauTemp)
        
        return True
        
    def find(self):
        # keysDict will be modified so make a copy of it.
        remainKeys = deepcopy(self.keysDict)
        hashSeedList = []
        # print maxTry
        for i in range(self.maxTry):
            newHashSeed = self.hashSeed + i*100;
            # smcho
            #print "SEED ", newHashSeed
            hashSeedList.append(newHashSeed)
            
            h = BloomierHasher(newHashSeed, self.m, self.k, self.q);
            # remainKeys = deepcopy(remainKeys)
            if self.findMatch(remainKeys, h):
                # The seed value is retreived from the index
                return OrderAndMatch(newHashSeed, self.piList, self.tauList)
            else:
                print "\n\nTry %d" % i
                remainKeys = deepcopy(self.keysDict)
            
        errorMessage = "Not found the match attempt -> %d (%s)" % (self.maxTry, hashSeedList)
        print >> sys.stderr, errorMessage
        raise Exception(errorMessage)
        return None
            
if __name__ == "__main__":
    keyMap = {"abc":10, "def":20, "abd":30}
    
    m = 4
    k = 3
    q = 5
    oamf = OrderAndMatchFinder(0, keyMap, m, k, q)
    oam = oamf.find()
    assert(oam is not None)
    print "PILIST", oam.piList
    print "TAULIST", oam.tauList
    #print oamf.getNeighbors("abc")
    
    #oamf.findMatch(k)
    # h = BloomierHasher(0, 10, 3, 5)
    # t = SingletonFindingTweaker(m, h)
    # key = "abc"
    # print key, t.tweak(key), t.getNeighborhood(key), "\n"
    # key = "abd"
    # print key, t.tweak(key), t.getNeighborhood(key), "\n"
    # key = "def"
    # print key, t.tweak(key), t.getNeighborhood(key), "\n"
    # 
    # # Even though key is not in the mapping, it returns value anyway
    # key = "aha"
    # print key, t.tweak(key), t.getNeighborhood(key), "\n"