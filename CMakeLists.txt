cmake_minimum_required(VERSION 3.10)

project(metadata)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_FLAGS "-O3 -Wall -Wextra")

file(GLOB_RECURSE sources "src/*.cpp")

add_executable(metadata ${sources})
target_include_directories(metadata PRIVATE /usr/include/id3)
target_link_libraries(metadata PRIVATE /usr/lib/libid3.so)



