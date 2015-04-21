#include "utilEncode.h"

namespace bloomier {
//using namespace std;
    
void UtilEncode::encode(int value, int length, unsigned char array[]) 
{
    int size_value = sizeof value;
    unsigned char bytes[size_value];
    
    //std::cout << size_value << std::endl;
    
    for (int i = 0; i < size_value; i++)
    {
        //std::cout << static_cast<unsigned char>(value >> (i*8)) << std::endl;
        bytes[i] = static_cast<unsigned char>(value >> (i*8));
    }
    
    int size_array = length; // sizeof(array) / sizeof(unsigned char);
    
    // if size_array is bigger than the integer, you need to fill in 0
    if (size_array > size_value) {
        for (int i = 0; i < size_value; i++)
        {
            array[i] = bytes[i];
        }
        for (int i = size_value; i < size_array; i++)
        {
            array[i] = 0;
        }
    } else { // size_array <= size_value
        for (int i = 0; i < size_array; i++)
        {
            // warning! truncate the value
            array[i] = bytes[i];
        }
    }
    return;
}

int UtilEncode::decode(unsigned char array[], int width)
{
    int result = 0;
    for (int i = 0; i < width; i++) {
        result += (array[i] << i * 8);
    }
    return result;
}

}