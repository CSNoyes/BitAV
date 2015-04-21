#ifndef __ORDER_AND_MATCH_H__
#define __ORDER_AND_MATCH_H__

using namespace std;

class OrderAndMatch
{
    int hashSeed;
    std::vector<std::string>* piList;
    std::vector<int>* tauList;
    int size;
public:
    OrderAndMatch(int hashSeed, std::vector<std::string>* piList, std::vector<int>* tauList) : 
        hashSeed(hashSeed), piList(piList), tauList(tauList) {}
        
    std::vector<std::string>* getPiList() {return piList;}
    std::vector<int>* getTauList() {return tauList;}
};

#endif