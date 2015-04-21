cmake_minimum_required(VERSION 3.1)
project(BloomBloomier)

# cmake -DCMAKE_BUILD_TYPE:STRING=Debug ../src
# http://www.cmake.org/Wiki/CMake_Useful_Variables#Compilers_and_Tools
set(CMAKE_CXX_FLAGS_DEBUG, ON)
set(CMAKE_CXX_COMPILER "/usr/bin/c++")
#set(CMAKE_CXX_COMPILER "/usr/bin/llvm-g++")
# http://stackoverflow.com/questions/5334095/cmake-multiarchitecture-compilation
set(CMAKE_CXX_FLAGS "-std=c++11 -m64")
# cmake -DCMAKE_OSX_ARCHITECTURES=x86_64

include_directories(/usr/local/include)
include_directories(.)
include_directories(./core)
link_directories(/usr/local/lib)
link_directories(./libs/bloomierFilter)

set(bloomier_srcs
    # bloomier filter code
    libs/bloomierFilter/BloomierFilter.cpp
    libs/bloomierFilter/core/util.cpp
    libs/bloomierFilter/core/utilEncode.cpp
    libs/bloomierFilter/core/hash.cpp
    libs/bloomierFilter/core/bloomierHasher.cpp
    libs/bloomierFilter/core/singletonFindingTweaker.cpp
    libs/bloomierFilter/core/orderAndMatchFinder.cpp
    )

add_library(bl ${bloomier_srcs})

set(md5_srcs
    libs/md5.cpp
    libs/md5wrapper.cpp
    )
add_library(md5 ${md5_srcs})


set(SOURCE_FILES
    main.cpp
    db.txt
    )


add_executable(BloomBloomier ${SOURCE_FILES})
target_link_libraries(BloomBloomier bl)
target_link_libraries(BloomBloomier md5)