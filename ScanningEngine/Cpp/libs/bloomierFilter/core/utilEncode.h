#ifndef __Util_Encode_H_
#define __Util_Encode_H_

#include <iostream>
#include <list>
#include <algorithm>

namespace bloomier {
    
/**
 * Utility class. All of the methods are static to be used 
 * as static function. 
 */

class UtilEncode {
public:
    /**
     * Given integer value, returns a byte array of width in size
     * The encoding is little endian 
     * With 5 byte array and value of 200 --> [200, 0, 0, 0, 0]
     * With 3 byte array and value of 256 --> [255, 1, 0]
     *
     * warning! truncate the value when the array is smaller than 4
     *
     *  @param int value
     *  @param unsigend char array[]
     *  @param width : the width of array, the array is just a pointer that has no size info.
     *                 You need to add this infomration also.
     */
     static void encode(int value, int width, unsigned char array[]);
     
    /*
     * Given array with size width, returns the value.
     */
     static int decode(unsigned char array[], int width);
};

} // namespace

#endif