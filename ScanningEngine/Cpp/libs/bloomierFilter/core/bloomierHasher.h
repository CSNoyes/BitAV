#ifndef __BLOOMIER_HASHER_H__
#define __BLOOMIER_HASHER_H__
#include <string>

namespace bloomier
{
class BloomierHasher
{
    int hashSeed;
    int m;
    int k;
    int q;
public:
    BloomierHasher(int hashSeed, int m, int k, int q) : hashSeed(hashSeed), m(m), k(k), q(q) {}
    void getNeighborhood(std::string key, unsigned char array[]);
    void getM(std::string key, unsigned char array[], int byteSize);
    
    // get method
    int getm() {return m;}
    int getk() {return k;}
    int getq() {return q;}
};
}
#endif