cmake_minimum_required(VERSION 3.15)
project(user-app CXX)

add_executable(user-app src/main.cpp)
find_package(webserver_wrapper)
target_link_libraries(user-app webserver_wrapper::webserver_wrapper)

install(TARGETS user-app DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        )
