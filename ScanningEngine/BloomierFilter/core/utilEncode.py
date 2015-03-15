# http://docs.python.org/2/library/struct.html
# http://stackoverflow.com/questions/16818463/python-encode-decoder-for-serialization-deserialization-javas-kyro-equivalence
# http://stackoverflow.com/questions/11624190/python-convert-string-to-byte-array
# http://stackoverflow.com/questions/2611858/struct-error-unpack-requires-a-string-argument-of-length-4
import struct
from commonUtil import *

def encode(value, width=1): 
    """
    We only take care of integer value
    width is the width of table in bytes: q = 8 --> width = 1
    """
    result = int2byteArray(value)
    if width < 4: # if widht is smaller than 4
        val = result[(4 - width):4]
    else:
        val = [0] * (width - 4) + result
    return val
    
def decode(value): # , formString = None):
    return byteArray2int(value)

if __name__ == "__main__":
    import sys
    sys.path.append("../../test/testcore")
    from testUtilEncode import *

    unittest.main(verbosity=2)
    