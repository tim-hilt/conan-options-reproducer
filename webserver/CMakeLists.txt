cmake_minimum_required(VERSION 3.15)
project(webserver CXX)

add_library(webserver src/webserver.cpp)
target_include_directories(webserver PUBLIC include)

find_package(3rdparty REQUIRED)

set_target_properties(webserver PROPERTIES PUBLIC_HEADER "include/webserver.hpp")
target_link_libraries(webserver 3rdparty::3rdparty)
install(TARGETS webserver)
