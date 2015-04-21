//
// Created by smcho on 5/30/13.
// Copyright (c) 2013 ___MPC___. All rights reserved.
//
// To change the template use AppCode | Preferences | File Templates.
//



#ifndef __BloomierFilter_H_
#define __BloomierFilter_H_

#include <map>
#include <vector>
#include <iostream>
#include <cstddef>
#include <cstring>
#include "core/util.h"
#include "core/utilEncode.h"
#include "core/bloomierHasher.h"
#include "core/orderAndMatchFinder.h"

namespace bloomier {

class BloomierFilter {
    int hashSeed;
    std::map<std::string, int>* keyMap;
    OrderAndMatchFinder* oam = NULL;
    OrderAndMatch* om = NULL;
    BloomierHasher* h = NULL;

    int m;
    int k;
    int q;
    int byteSize;

    unsigned char *table = NULL;
    // not size optimal, only for testing purposes
    int *valueTable = NULL;
public:
    BloomierFilter(int hashSeed, std::map<std::string, int>* keyMap, int m, int k, int q);
    ~BloomierFilter();
    void create(std::map<std::string, int>* keyMap, OrderAndMatchFinder* oam);
    bool get(std::string key, int& value);
    bool set(std::string key, int value);
};

}
#endif //__BloomierFilter_H_
