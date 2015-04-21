#include "util.h"
#include "singletonFindingTweaker.h"

using namespace std;
namespace bloomier {
    
SingletonFindingTweaker::SingletonFindingTweaker(map<string, int> keyMap, BloomierHasher* h)
{
    // : keyMap(keyMap), h(h) {};
    this->keyMap = keyMap;
    this->h = h;
    int k = h->getk();
    unsigned char neighborhood[k];
    
    // for each keyMap
    for (auto ip = keyMap.begin(); ip != keyMap.end(); ++ip)
    {
        // get neighbors
        //cout << ip->first << endl;
        string key = ip->first;
        h->getNeighborhood(key, neighborhood);
        for (int i = 0; i < h->getk(); i++)
        {
            // it's already found, so it's in the nonSingletons
            if (Util::in(hashesSeen, neighborhood[i]))
            {
                nonSingletons.insert(neighborhood[i]);
            }
        }
        
        // insert all the hashes that I found in the hashesSeen set
        for (int i = 0; i < k; i++)
        {
            hashesSeen.insert(neighborhood[i]);
        }
    }
} 

int SingletonFindingTweaker::tweak(std::string key)
{
    int k = h->getk();
    //  void getNeighborhood(std::string key, unsigned char array[]);
    unsigned char result[k];
    h->getNeighborhood(key, result);
    
    //Util::print(result, k);
    for (int i = 0; i < k; i++)
    {
        //std::cout << i << ":" << int(result[i]) << std::endl;
        if (!Util::in(nonSingletons, int(result[i])))
            return i; // result[i];
    }
    // return -1 means not found
    return -1;
}

}
