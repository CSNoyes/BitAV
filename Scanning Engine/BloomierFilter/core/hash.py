import hashlib, uuid
# http://stackoverflow.com/questions/209513/convert-hex-string-to-int-in-python

def getHash(key, hashseed, m, k):
    """
    We use sha256, and it generates 64 bytes of hash number, so k should be 2 <= k <= 32
    However, because of duplicity the real limit should be much lower.
    
    Todo: You can concatenate more sha256 values to get more k values
    """
    salt = str(hashseed)
    hashed_password = hashlib.sha256(key + salt).hexdigest()
    #print hashed_password
    if k > 32: raise Exception("k should be less than 32")
    if k <= 1: raise Exception("k should be more than 2")
    if k > m: raise Exception("k should be less than m")
    
    # it cuts 4 byte from the hashed_password, so the value is 0xFFFFFFFF
    assert(m < 0xFFFFFFFF)
    hashedPasswordLength = len(hashed_password)
    assert(hashedPasswordLength/4 > k)

    result = set()
    index = 0
    
    # make the non-overwrapping hash value below m
    while True:
        value = int(hashed_password[index:index+4], 16) % m
        index += 4
        result.add(value)
        
        if len(result) == k: break
        assert index < hashedPasswordLength
        
    return list(result)
    
if __name__ == "__main__":
    res = getHash("abcd", 1, 100, 5) # seed:1, m = 10, k = 5
    print res
    assert len(res) == 5
    
    res = getHash("abcd", 3, 100, 5) # seed:1, m = 10, k = 5
    print res
    assert len(res) == 5
    
    res = getHash("abc", 0, 4, 3) # seed:1, m = 10, k = 5
    print res
    
    res = getHash("abc", 1, 4, 3) # seed:1, m = 10, k = 5
    print res
