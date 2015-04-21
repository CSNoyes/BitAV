#include "orderAndMatchFinder.h"
#include "util.h"
#include "singletonFindingTweaker.h"

namespace bloomier 
{

OrderAndMatchFinder::OrderAndMatchFinder(int hashSeed, std::map<std::string, int>* keyMap, int m, int k, int q, int maxTry)
{
    this->hashSeed = hashSeed;
    this->keyMap = keyMap;
    this->m = m;
    this->k = k;
    this->q = q;
    this->maxTry = maxTry;
    
    h = NULL;
    //h = new BloomierHasher(hashSeed, m, k, q);
}

OrderAndMatchFinder::~OrderAndMatchFinder() {
    if (h != NULL) delete h;
    if (oa != NULL) delete oa;
}

bool OrderAndMatchFinder::findMatch(std::map<std::string, int>& remainingKeysDict)
{
    if (remainingKeysDict.empty()) return true;
    std::vector<std::string> piTemp;
    std::vector<int> tauTemp;
    
    auto tweaker = SingletonFindingTweaker(remainingKeysDict, h);
    for (auto i = remainingKeysDict.begin(); i != remainingKeysDict.end(); ++i)
    {
        string key = i->first;
        // out of the k values [1, 10, 20], tweaker returns the location where it doesn't share with others
        // tweaker returns -1 when it can't find the 
        auto res = tweaker.tweak(key);
        //std::cout << res << std::endl;
        if (res != -1) {
            tauTemp.push_back(res);
            piTemp.push_back(key);
        }
    }
    
    if (piTemp.empty()) return false;
    
    Util::removeAll(remainingKeysDict, piTemp);
    if (!remainingKeysDict.empty())
        if (findMatch(remainingKeysDict) == false)
        return false;
        
    Util::addAll(piList, piTemp);
    Util::addAll(tauList, tauTemp);
    return true;
}

OrderAndMatch* OrderAndMatchFinder::find()
{
    std::map<std::string, int> copied;
    Util::deepcopy(*(this->keyMap), copied);
    
    for (int i = 0; i < maxTry; i++)
    {
        int newHashSeed = hashSeed + i;
        if (h != NULL) delete h;
        h = new BloomierHasher(hashSeed, m, k, q);
        if (findMatch(copied)) {
            oa = new OrderAndMatch(newHashSeed, &piList, &tauList);
            return oa;
        }
    }
    if (oa != NULL) delete oa; oa = NULL;
    return oa;
}

}