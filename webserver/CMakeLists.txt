cmake_minimum_required(VERSION 3.15)
project(webserver CXX)

add_library(webserver src/webserver.cpp)
target_include_directories(webserver PUBLIC include)

set_target_properties(webserver PROPERTIES PUBLIC_HEADER "include/webserver.hpp")
install(TARGETS webserver)
