import ScanningEngine.Python.BloomierFilter.bloomierFilter as bloomier
import ScanningEngine.Python.BloomFilter.fastFilter as bloom

class ffBF:
    # feedforward bloom-bloomier mechanism
    def __init__(self, values, p):
        # n: number of elements
        # p: desired false positive rate
        self.n = len(values)
        self.p = p
        self.bloomFilter = bloom.bloomFilter(self.n,p)
        self.bloomierFilter = bloomier.BloomierFilter(values,p)

        for malSig in values:
            self.bloomFilter.add(malSig)

    def lookup(self, suspect):
        if self.bloomFilter.lookup(suspect):
            bloomierTest = self.bloomierFilter.get(suspect)
            if not bloomierTest:
                return False
            elif bloomierTest:
                if suspect == bloomierTest:
                    return True
        else:
            return False

    def add(self, sig):
        if self.lookup(sig):
            return False
        else:
            self.bloomFilter.add(sig)
            self.bloomierFilter.set(sig,sig)