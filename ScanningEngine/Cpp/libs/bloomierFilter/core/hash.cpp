#include <string>
#include <set>
#include <random>
#include <assert.h>
#include <locale>
#include <sstream>
#include <iostream>
#include "hash.h"

using namespace std;
namespace bloomier {
    
string Hash::getHashString(string key, int hashSeed)
{
    string newkey = to_string(hashSeed) + key;

    locale loc;                 // the "C" locale
    const collate<char>& coll = use_facet<collate<char> >(loc);
    unsigned long myhash = coll.hash(newkey.data(),newkey.data()+newkey.length());
    // cout << myhash << endl;
    
    // the value is long size, so 20 byte size hash is created.
    // we split the values by 2, so m should be less than 100 and k should be less than stringsize/2
    // 12412447795099120871
    
    std::stringstream strstream;
    strstream << myhash;
    string hashString = strstream.str();
    return hashString;
}

void Hash::getHash(string key, int hashSeed, int m, int k, unsigned char result[])
{
    assert(k >= 1);
    assert(m >= 1);

    // returned hash string is too short, so make 4 to concatenate them
    hashSeed*100;
    string key1 = getHashString(key, hashSeed);
    string key2 = getHashString(key, hashSeed + 1000);
    string key3 = getHashString(key, hashSeed - 1000);
    string key4 = getHashString(key, hashSeed + 2000);
    string key5 = getHashString(key, hashSeed - 2000);
    string key6 = getHashString(key, hashSeed + 3000);
    string key7 = getHashString(key, hashSeed - 3000);
    string key8 = getHashString(key, hashSeed + 4000);
    string hashString = key1 + key2 + key3 + key4 + key5 + key6 + key7 + key8;
    
    // we cut the string by 4, so the maximum m value is 9999
    assert(hashString.size()/4 > k);
    //cout << hashString.size() << endl;
    
    int index = 0;
	int step = 4;
    set<int> values;
    while (true) {
        if (index >= hashString.size()) break;
        int candiate = atoi((hashString.substr(index,  step)).c_str()) % m;
        // cout << hashString.substr(index,  step) << ":" << candiate << endl;
        values.insert(candiate);
        index += step;
        if (values.size() == k) break;
    }
    
    //cout << "***" << values.size() << endl;
    int i = 0;
    for (auto it = values.begin(); it != values.end(); ++it) {
        //cout << *it << endl;
        result[i] = *it;
        i++;
    }
}    
}