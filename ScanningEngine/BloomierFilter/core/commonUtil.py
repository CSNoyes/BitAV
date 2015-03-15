import inspect
import os.path
import sys
import struct

def dprint(string):
    # http://stackoverflow.com/questions/3711184/how-to-use-inspect-to-get-the-callers-info-from-callee-in-python
    # http://stackoverflow.com/questions/3056048/filename-and-line-number-of-python-script
    frame,filename,line_number,function_name,lines,index=\
            inspect.getouterframes(inspect.currentframe())[1]
    print >> sys.stderr,  str(string) + "\t\t\t(%s:%d)" % (os.path.basename(filename), line_number)
    
def sprint(string, format = "hex", silent = False):
    """
    Serialized data printer
    """
    result = ""
    for i in string:
        if format == "hex":
            result += "[%s]" % hex(ord(i))
        else:
            result += "[%d]" % ord(i)

    if not silent:
        print result
        
    return result
    
def string2byteArray(string):
    result = []
    for val in string:
        result.append(ord(val))
    return result
    
def byteArray2string(array, width=4):
    """
    http://stackoverflow.com/questions/17077257/integer-array-to-string-in-python
    [1,2,3,4] => '\x01\x02\x03\x04'
    """
    result = ''.join([chr(x) for x in array])
    return result[4-width:4]
    
def int2byteArray(value):
    """
    integer value decomposer
    """
    a = value >> 0 & 0x000000FF
    b = value >> 8 & 0x000000FF
    c = value >> 16 & 0x000000FF
    d = value >> 24 & 0x000000FF
    return [d,c,b,a] # big endian
    
def byteArray2int(array):
    assert type(array) is list
    length = len(array)
    if length < 4:
        array = [0]*(4 - length) + array
    
    res = (array[0] << 24) + (array[1] << 16) + (array[2] << 8) + (array[3])
    return res
    
def int2string(value, width = 4):
    return byteArray2string(int2byteArray(value), width)
    
def string2int(string):
    return byteArray2int(string2byteArray(string))
    
def map2string(m):
    """
    key is string
    value is integer
    """
    result = ""
    for key, value in m.items():
        length = int2string(len(key))
        varray = int2string(value)
        result += (length + key + varray)
        
    return result
    
def string2map(string):
    m = {}
    stringLength = len(string)
    if stringLength == 0: return m
    
    i = 0
    while (i < stringLength):
        length = string2int(string[i:i+4])
        key = string[i+4:i+4+length]
        value = string2int(string[i+4+length:])
        i += (4 + length + 4) # 4 is for length storage, length is string length and 4 is value length
        # print length
        # print key
        # print value
        m[key] = value
    
    return m
    
if __name__ == "__main__":
    sys.path.append("../../test/testcore")
    from testCommonUtil import *
    unittest.main(verbosity=2)