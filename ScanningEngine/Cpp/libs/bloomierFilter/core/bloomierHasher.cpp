#include <iostream>
#include <locale>
#include <sstream>
#include "hash.h"
#include "bloomierHasher.h"

using namespace std;

namespace bloomier
{

void BloomierHasher::getNeighborhood(string key, unsigned char result[])
{
    Hash::getHash(key, hashSeed, m, k, result);
    // for (int i = 0; i < k; i++)
    // {
    //     cout << result[i] << endl;
    // }
}

void BloomierHasher::getM(string key, unsigned char array[], int byteSize)
{
    locale loc;
    const collate<char>& coll = use_facet<collate<char> >(loc);
    int seed = coll.hash(key.data(),key.data()+key.length());
    srand (seed);
    for (int i = 0; i < byteSize; i++)
        array[i] = rand() % 255;
}
}