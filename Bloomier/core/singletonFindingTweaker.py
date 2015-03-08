from bloomierHasher import *
PRINT = False

class SingletonFindingTweaker:
    def __init__(self, keysDict, hasher):
        self.keysDict = keysDict
        self.hasher = hasher
        
        hashesSeen = set()
        nonSingletons = set()
        
        for k in self.keysDict:
            if PRINT:
                print hasher.getNeighborhood(k)
            # for all the neighborhoods for each of the key
            for neighborhood in hasher.getNeighborhood(k):
                if neighborhood in hashesSeen:
                    nonSingletons.add(neighborhood)
            
            for neighborhood in hasher.getNeighborhood(k):    
                hashesSeen.add(neighborhood)
        """
        The neighbors are 
        [0, 5, 7] <- first singleton is "0" <-- index 0
        [3, 8, 6] <- first singleton is "1" <-- index 1
        [6, 3, 2] <- first singleton is "2" <-- index 2
        
        set([0, 2, 3, 5, 6, 7, 8])
        set([3, 6]) <-- Only "6" is duplicated, so all the others are singleton
        """
        self.nonSingletons = nonSingletons
        #print hashesSeen
        #print nonSingletons
        
    def __str__(self):
        result = "Nonsingletons > " + str(self.nonSingletons) + "\n"
        return result
        
    def tweak(self, key):
        """
        tweak returns the index of the neighbors that is singleton
        """
        i = 0
        #print key, h.getNeighborhood(key)
        for n in self.hasher.getNeighborhood(key):
            #print "?", n
            if not (n in self.nonSingletons):
                #print "*", n
                return i
            i += 1
        return None
        
    def getNeighborhood(self, key):
        return self.hasher.getNeighborhood(key)
                
if __name__ == "__main__":
    h = BloomierHasher(0, 10, 3, 5)
    k = {"abc":10, "def":20, "abd":30}
    t = SingletonFindingTweaker(k, h)
    # abc [0, 5, 7]
    print t.tweak("abc") # returns 0 [0 <-,5,7]
    # def [6, 3, 2]
    print t.tweak("def") # returns 2 [3, 8, 6 <-]
    # abd [3, 8, 6]
    print t.tweak("abd") # returns 1 [6, 3 <-, 2]
