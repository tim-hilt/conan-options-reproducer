cmake_minimum_required(VERSION 3.15)
project(user-app CXX)

add_executable(user-app src/main.cpp)
find_package(webserver)
target_link_libraries(user-app webserver::webserver)

install(TARGETS user-app DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        )
