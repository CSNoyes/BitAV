#ifndef __ORDER_AND_MATCH_FINDER_H__
#define __ORDER_AND_MATCH_FINDER_H__

#include <map>
#include <vector>
#include <cstddef>
#include "bloomierHasher.h"
#include "orderAndMatch.h"

namespace bloomier {

class OrderAndMatchFinder
{
    int hashSeed;
    std::map<std::string, int>* keyMap;
    int m;
    int k;
    int q;
    int maxTry;
    std::vector<std::string> piList;
    std::vector<int> tauList;
    BloomierHasher *h = NULL;
    OrderAndMatch *oa = NULL;
public:
    OrderAndMatchFinder(int hashSeed, std::map<std::string, int>*, int m, int k, int q, int maxTry = 10);
    ~OrderAndMatchFinder();
    
    /**
     * findMatch() method finds 
     */
    bool findMatch(std::map<std::string, int>& remainingKeysDict);
    OrderAndMatch* find();
    OrderAndMatch* getOrderAndMatch() {return oa;}
    std::vector<std::string>* getPiList() {return &piList;}
    std::vector<int>* getTauList() {return &tauList;}
        
    int getHashSeed() {return hashSeed;}
    int getm() {return m;}
    int getk() {return k;}
    int getq() {return q;}
    
};

}

#endif