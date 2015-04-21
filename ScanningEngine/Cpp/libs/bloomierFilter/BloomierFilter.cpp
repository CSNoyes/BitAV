//
// Created by smcho on 5/30/13.
// Copyright (c) 2013 ___MPC___. All rights reserved.
//
// To change the template use AppCode | Preferences | File Templates.
//


#include "BloomierFilter.h"

namespace bloomier {

    BloomierFilter::BloomierFilter(int hashSeed, std::map<std::string, int>* keyMap, int m, int k, int q)
    {
        this->hashSeed = hashSeed;
        this->keyMap = keyMap;
        this->m = m;
        this->k = k;
        this->q = q;

        //std::cout << "K" << this->k << endl;
        byteSize = Util::getByteSize(q);
        oam = new OrderAndMatchFinder(hashSeed, keyMap, m, k, q);
        om = oam->find();
        h = new BloomierHasher(hashSeed, m, k, q);

        table = new unsigned char[byteSize * m];
        // not size optimal, only for testing purposes
        valueTable = new int[m];

        create(keyMap, oam);
    }

    BloomierFilter::~BloomierFilter()
    {
        if (oam != NULL) delete oam;
        // if (om != NULL) delete om; om is deleted automatically from oam.
        if (table != NULL) delete table;
        if (valueTable != NULL) delete valueTable;
        if (h != NULL) delete h;
    }

    void BloomierFilter::create(std::map<std::string, int>* keyMap, OrderAndMatchFinder* oam)
    {
        auto piList = oam->getPiList();
        auto tauList = oam->getTauList();

        unsigned char neighbors[k];
        unsigned char mask[byteSize];
        unsigned char encodedValue[byteSize];

        //Util::print(piList);
        //Util::print(tauList);

        //int i = 0;
        int keySize = piList->size();
        for (int i = 0; i < keySize; i++)
            // auto ip = piList->begin(); ip != piList->end(); ++ip)
        {
            std::string key = (*piList)[i];
            h->getNeighborhood(key, neighbors);
            //Util::print(neighborhood, k);
            h->getM(key, mask, byteSize);
            //Util::print(mask, byteSize);

            int value = (*keyMap)[key];
            int l = (*tauList)[i];
            int L = neighbors[l];

            UtilEncode::encode(l, byteSize, encodedValue);
            //Util::print(encodedValue, byteSize);

            Util::byteArrayXor(encodedValue, mask, byteSize);

            for (int i = 0; i < k; i++)
            {
                if (i == l) continue;
                int v = neighbors[i];
                Util::byteArrayXor(encodedValue, table + byteSize*v, byteSize);
            }

            Util::setInArray(table + byteSize*L, encodedValue, byteSize);
            valueTable[L] = value;
            //int index =
            //std::cout << i << "?" << key << ':' << value << "*" << l << std::endl;
            //i++;
        }
    }

/*
 * Code duplication with get value
 */
    bool BloomierFilter::set(std::string key, int value)
    {
        unsigned char neighbors[k];
        unsigned char mask[byteSize];
        unsigned char valueToGet[byteSize]; // = {0};
        memset(valueToGet, 0, sizeof(unsigned char)*byteSize);

        h->getNeighborhood(key, neighbors);
        h->getM(key, mask, byteSize);

        Util::byteArrayXor(valueToGet, mask, byteSize);
        for (int i = 0; i < k; i++)
        {
            int v = neighbors[i];
            Util::byteArrayXor(valueToGet, table + byteSize*v, byteSize);
        }

        //Util::xorOperations(valueToGet, mask, n)
        int l = UtilEncode::decode(valueToGet, byteSize);

        if (l < m) {
            int L = neighbors[l];
            valueTable[L] = value;
            return true;
        }

        return false;
    }

    bool BloomierFilter::get(std::string key, int& value)
    {
        unsigned char neighbors[k];
        unsigned char mask[byteSize];
        unsigned char valueToGet[byteSize]; // = {0};
        memset(valueToGet, 0, sizeof(unsigned char)*byteSize);

        h->getNeighborhood(key, neighbors);
        h->getM(key, mask, byteSize);

        Util::byteArrayXor(valueToGet, mask, byteSize);
        for (int i = 0; i < k; i++)
        {
            int v = neighbors[i];
            Util::byteArrayXor(valueToGet, table + byteSize*v, byteSize);
        }

        //Util::xorOperations(valueToGet, mask, n)
        int l = UtilEncode::decode(valueToGet, byteSize);

        if (l < m) {
            int L = neighbors[l];
            value = valueTable[L];
            return true;
        }

        return false;
    }

}