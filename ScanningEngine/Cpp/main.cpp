/*
 **************************************************************************
 * Copyright notice:                                                      *
 * Free use of the Bloom Filter Library is permitted under the guidelines *
 * and in accordance with the most current version of the Common Public   *
 * License.                                                               *
 * http://www.opensource.org/licenses/cpl1.0.php                          *
 *                                                                        *
 **************************************************************************
 */

/*
 Description: This example demonstrates basic usage of the Bloom filter.
 Initially some values are inserted then they are subsequently
 queried, noting any false positives or errors.
 */
#include <ctime>
#include <fstream>
#include <iostream>
#include "libs/bloomFilter/bloom_filter.hpp"
#include "libs/bloomierFilter/BloomierFilter.h"
#include <libs/md5wrapper.h>
#include <math.h>


using namespace std;

class bloomBloomier
{

public:
    bloom_filter* blmFilter;
    bloomier::BloomierFilter* blmrFilter;
    void instantiate(int n, float p){
        blmFilter = instBloom(n,p);

        initSignatureDatabase(blmFilter);

        map<string, int>* keyMap =  blmFilter->getKVs();

        long int j = keyMap->size();
        cout << keyMap->size();
        int m = (-j * log(0.01) / pow(log(2),2));
        int k = 0.7 * (m/n);
        if (k < 1){
            k = 1;
        }
        int q = log(k/0.05);

        blmrFilter = new bloomier::BloomierFilter(0, keyMap, m, k, q);

    }

    //creates bloom filter
    bloom_filter* instBloom(int n, float p){
        bloom_parameters parameters;

        // expected element count
        parameters.projected_element_count = n;

        // false probability allowance
        parameters.false_positive_probability = p; // 1 in 10000

        parameters.compute_optimal_parameters();

        bloom_filter* filter = new bloom_filter(parameters);

        return filter;
    }

    //loads bloom filter
    void initSignatureDatabase(bloom_filter* filter){
        ifstream keys;


        keys.open("/Users/Charlie/ClionProjects/BloomBloomier/dbSmallS.txt");

        if (keys.is_open() == false) {
            cout << "not open";
        }

        string line;
        while( getline(keys, line) ) {
            int start = line.find(":");
            string substring = line.substr(start + 1, (start + 33) - (start) - 1);
            filter->insert(substring);

        }

    }

    bool checkFile(string signature){
        if (blmFilter->contains(signature)) {
            int hashCode = blmFilter->hashCode(signature);
            if (blmrFilter->get(blmFilter->lastIndice,hashCode)){
                return true;
            }
            return false;
        }
        else{
            return false;
        }
    }



    void test(){
        md5wrapper md5;
        vector<string> filePaths;

        for( int a = 1; a <= 1; a++ ) {
            string path = "/Users/Charlie/ClionProjects/BloomBloomier/samples/";
            path += to_string(a);
            filePaths.push_back(path);
        }
        clock_t start = clock();
        vector<string> hashes = md5.getHashFromFiles(md5.getFileVector(filePaths));
        for (string hash : hashes){
            checkFile(hash);
        }
        clock_t end = clock();
        double elapsed_secs = double(end - start) / CLOCKS_PER_SEC;
        cout << endl << elapsed_secs;

    }
};

int main()
{
    vector<string> knownPatterns;

    bloomBloomier mechanism;
    mechanism.instantiate(55000,0.01);
    mechanism.test();
    return 0;
}

