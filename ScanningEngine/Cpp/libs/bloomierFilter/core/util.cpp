//
// Created by smcho on 5/30/13.
// Copyright (c) 2013 ___MPC___. All rights reserved.
//
// To change the template use AppCode | Preferences | File Templates.
//

#include "util.h"

namespace bloomier {

template <class T>
void Util::addAll(std::vector<T>& aList, const std::vector<T> bList)
{
    // copy all the elements in bList list into aList
    for (auto it = bList.begin(); it != bList.end(); ++it)
    {
        aList.push_back(*it);
    }
}
// specialization
template void Util::addAll<std::string>(std::vector<std::string>&, const std::vector<std::string>);
template void Util::addAll<int>(std::vector<int>&, const std::vector<int>);

template <class T1, class T2, class T3>
void Util::removeAll(std::map<T1, T2>& aMap, const std::vector<T3> bList)
{
    std::list<T1> keys;
    // 1. get all the keys that has the elements from bList
    for (auto it = bList.begin(); it != bList.end(); ++it)
    {
        for (auto j = aMap.begin(); j != aMap.end(); ++j)
        {
            if (j->first == *it) keys.push_back(j->first);
        }
    }
    // 2. remove all the items of the key
    for (auto it = keys.begin(); it != keys.end(); ++it)
    {
        aMap.erase(*it);
    }
}
template void Util::removeAll(std::map<std::string, int>& , const std::vector<std::string>);

void Util::byteArrayXor(unsigned char* result, const unsigned char* input, int size)
{
    //int size = std::min(sizeof(result)/sizeof(unsigned char), sizeof(input)/sizeof(unsigned char));

    for (int i = 0; i < size; i++)
    {
        result[i] = result[i] ^ input[i];
    }
}

void Util::setInArray(unsigned char* result, const unsigned char* input, int size)
{
    for (int i = 0; i < size; i++)
    {
        result[i] = input[i]; // ^ input[i];
    }
}

// void Util::byteArrayXor(unsigned char result[], const unsigned char* input, int byteSize)
// {
//     for (int i = 0; i < byteSize; i++)
//     {
//         unsigned char value = input[i];
//         result[i] = result[i] ^ value;
//     }
// }

int Util::getByteSize(int value)
{
    // return q//8 + (1 if q % 8 != 0 else 0
    return value / 8 + (value % 8 == 0 ? 0 : 1);
}

bool Util::in(std::set<int> setArray, int value)
{
    auto it = setArray.find(value);
    if (it == setArray.end()) // not found
        return false;
    else
        return true;
}

template <class T>
bool Util::in(std::vector<T> vectorArray, T value)
{
    auto it = find(vectorArray.begin(), vectorArray.end(), value);
    if (it == vectorArray.end()) return false;
    return true;
}
template bool Util::in(std::vector<int> vectorArray, int value);
template bool Util::in(std::vector<std::string> vectorArray, std::string value);

void Util::deepcopy(const std::map<std::string, int> source, std::map<std::string, int>& dest)
{
    for (auto it = source.begin(); it != source.end(); ++it)
    {
        //std::cout << it->first << ":" << it->second << std::endl;
        dest[it->first] = it->second;
    }
}

// debugging functions
template <class T>
void Util::print(std::vector<T>* vectorArray)
{
    for (auto i = vectorArray->begin(); i != vectorArray->end(); ++i)
    {
        std::cout << *i << ":";
    }
    std::cout << std::endl;
}
template void Util::print(std::vector<int>* vectorArray);
template void Util::print(std::vector<std::string>* vectorArray);
  
template <class T>
void Util::print(std::vector<T> vectorArray)
{
    for (auto i = vectorArray.begin(); i != vectorArray.end(); ++i)
    {
        std::cout << *i << ":";
    }
    std::cout << std::endl;
}
template void Util::print(std::vector<int> vectorArray);
template void Util::print(std::vector<std::string> vectorArray);

template <class T>
void Util::print(T* array, int size)
{
    std::cout << "ARRAY PRINT:" << size << "<";
    for (int i = 0; i < size; i++)
    {
        std::cout << int(array[i]) << ":";
    }
    std::cout << std::endl;
}
template void Util::print(int* vectorArray, int);
//template void Util::print(std::string* vectorArray, int);
template void Util::print(unsigned char* vectorArray, int);

} // namespace
