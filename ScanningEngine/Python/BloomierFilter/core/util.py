import sys

def addAll(aList, elements):
    # assert type(elements) is list
    # assert type(aList) is list
    for e in elements:
        aList.append(e)
        
def removeAll(aDict, elements):
    # assert type(elements) is list
    # assert type(aDict) is dict
    for e in elements:
        if e in aDict:
            del aDict[e]
            
def byteArrayXor(result, input2):
    # assert type(result) is list
    # assert type(input2) is list
    
    length = min(len(result), len(input2))
    for index in range(length):
        result[index] = result[index] ^ input2[index]
        
def getByteSize(q):
    return q//8 + (1 if q % 8 != 0 else 0)
    
if __name__ == "__main__":
    sys.path.append("../../test/testcore")
    from testUtil import *
    
    unittest.main(verbosity=2)
    
    # # getByteSize
    # q = 9
    # assert 2 == getByteSize(q)
    # 
    # # byteArrayXor 
    # input1 = [255, 0]
    # input2 = [0, 255]
    # byteArrayXor(input1, input2)
    # assert input1 == [255, 255]
    # input1 = [255, 255]
    # input2 = [255, 255]
    # #print input1
    # byteArrayXor(input1, input2)
    # #print input1
    # assert input1 == [0, 0]
    # 
    # # addAll simple unit test
    # a = []
    # addAll(a, ['b','c'])
    # assert a == ['b','c']
    # 
    # # removeAll simple unit test
    # a = {'a':10, 'b':20, 'c':30}
    # removeAll(a, ['a','c'])
    # assert len(a) == 1
    # assert a['b'] == 20, "ERROR b should be 20 , but we have %d" % a['b']