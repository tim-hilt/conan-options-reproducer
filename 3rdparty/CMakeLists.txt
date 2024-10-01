cmake_minimum_required(VERSION 3.15)
project(3rdparty CXX)

add_library(3rdparty src/3rdparty.cpp)
target_include_directories(3rdparty PUBLIC include)

set_target_properties(3rdparty PROPERTIES PUBLIC_HEADER "include/3rdparty.hpp")
install(TARGETS 3rdparty)
