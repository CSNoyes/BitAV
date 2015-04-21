#ifndef __SINGLETON_FINDING_TWEAKER_H__
#define __SINGLETON_FINDING_TWEAKER_H__

#include <map>
#include <set>
#include <vector>
#include "bloomierHasher.h"

using namespace std;

namespace bloomier {
    
class SingletonFindingTweaker
{
    map<string, int> keyMap;
    
    BloomierHasher* h;
    set<int> nonSingletons;
    set<int> hashesSeen;
    
public:
    SingletonFindingTweaker(map<string, int> keyMap, BloomierHasher* h); // : keyMap(keyMap), h(h) {};
    
    /**
     * tweak returns the index of the neighbors that is singleton
     * "abc" --> [1, 3, 4] as neighbors
     * tweak returns the first number in the neighbors that is not shared by others
     * 
     */
    int tweak(string key);
};
    
} // namespace

#endif