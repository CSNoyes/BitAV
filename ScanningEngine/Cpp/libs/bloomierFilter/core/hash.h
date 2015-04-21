#ifndef __HASH_H__
#define __HASH_H__

namespace bloomier
{
class Hash
{
    static std::string getHashString(std::string key, int hashSeed);
public:
    /*
     * getHash : return result[size] as the hash array
     * @param string key : the key value
     * @param int hashSeed : the seed value
     * @param int m : m is the number of row in table
     * @param int k : the number of hash value
     * @param unsigned char result[] : the array where the result is stored
     *
     * Warning: we use collate C++ method to get hash from the key, however the 
     * generated hash value too short and we concatenate 8 hash numbers.
     * The total hash size is around 120, but we cut them as 4, so the accessible hash number
     * is around 30. Be careful this is enough or not.
     */
    static void getHash(std::string key, int hashSeed, int m, int k, unsigned char result[]);    
};
}
#endif