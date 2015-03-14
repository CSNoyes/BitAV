from random import Random
from hash import *
from util import *

class BloomierHasher:
    def __init__(self, hashSeed, m, k, q):
        self.hashSeed = hashSeed
        self.m = m
        self.k = k
        self.q = q
        
        # hold the enough byte size for q
        self.byteSize = getByteSize(q) # self.q//8 + (1 if self.q % 8 != 0 else 0)
        # smcho
        #print "SEED > ", self.hashSeed
        
    def __str__(self):
        result = "m(%d)k(%d)q(%d)seed(%d)" % (self.m,self.k,self.q,self.hashSeed)
        return result
        
    def getNeighborhood(self, key):
        """
        Given key, returns 'k' hash values
        """
        #print hash(key)
        # http://stackoverflow.com/questions/9755538/how-do-i-create-a-list-of-unique-random-numbers
        
        hashResult = getHash(key, self.hashSeed, self.m, self.k)
        # smcho
        #print key, "** hashResult > ", hashResult, "seed: ", self.hashSeed
        return hashResult
        #return random.sample(range(self.m), self.k)
        
        #return (int(random()*self.m*10 % self.m), self.k)
        #return ( for _ in range(self.k))
        
    def getM(self, key):
        """
        Given key, returns M for xoring the output
        As the output is q bits, the value should be large enough to cover it
        byte[q//8 + 1]
        """
        #print hash(key)
        random = Random(key)
        
        return random.sample(range(256), self.byteSize)
        #random = Random(key*2).random
        #return (int(random()*self.m*10 % 256) for _ in range(self.q//8 + 1))
        
if __name__ == "__main__":
    b = BloomierHasher(0, 100, 10, 16)
    print "---\nNeighbors\n---"
    for i in b.getNeighborhood("ABC"):
        print i
        
    print "---\nMask values\n---"
    for i in b.getM("ABC"):
        print i
        
    """
    Diffrenet hash seed, but the Mask value is the same
    """
    b = BloomierHasher(1, 100, 10, 16)
    print "---\nNeighbors\n---"
    for i in b.getNeighborhood("ABC"):
        print i

    print "---\nMask values\n---"
    for i in b.getM("ABC"):
        print i
