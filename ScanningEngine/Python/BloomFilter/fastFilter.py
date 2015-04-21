from pyhashxx import hashxx
from math import log

class bloomFilter:
    # the smallest counting bloom filter I can make
    def __init__(self, n, p):
        # n: number of elements
        # m: size of filter (buckets)
        # k: number of hash functions
        # p: desired false positive rate

        self.m = int(abs(((n*log(p))/(log(2)**2))))
        self.n = n
        self.k = int((self.m/n * log(2)))
        self.filterArr = [0] * self.m

    def add(self, string):
        for seed in xrange(self.k):
            result = hashxx(string + str(seed)) % self.m
            self.filterArr[result] += 1

    def lookup(self, string):
        for seed in xrange(self.k):
            result = hashxx(string + str(seed)) % self.m
            if self.filterArr[result] == 0:
                return False
        return True

    def delete(self, string):
        if self.lookup(string):
            for seed in xrange(self.k):
                result = hashxx(string + str(seed)) % self.m
                self.filterArr[result] -= 1

        else:
            print "Attempted deletion of non-present element(s)."