cmake_minimum_required(VERSION 3.15)
project(webserver_wrapper CXX)

add_library(webserver_wrapper src/webserver_wrapper.cpp)
target_include_directories(webserver_wrapper PUBLIC include)

find_package(webserver REQUIRED)

set_target_properties(webserver_wrapper PROPERTIES PUBLIC_HEADER "include/webserver_wrapper.hpp")
target_link_libraries(webserver_wrapper webserver::webserver)
install(TARGETS webserver_wrapper)
