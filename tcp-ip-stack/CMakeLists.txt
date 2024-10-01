cmake_minimum_required(VERSION 3.15)
project(tcp_ip CXX)

add_library(tcp_ip src/tcp_ip.cpp)
target_include_directories(tcp_ip PUBLIC include)

find_package(3rdparty REQUIRED)

set_target_properties(tcp_ip PROPERTIES PUBLIC_HEADER "include/tcp_ip.hpp")
target_link_libraries(tcp_ip 3rdparty::3rdparty)
install(TARGETS tcp_ip)
