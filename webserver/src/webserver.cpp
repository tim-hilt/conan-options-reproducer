#include <iostream>
#include "webserver.hpp"

void printFoo()
{
#ifdef FOO
    std::cout << FOO << "\n";
#else
    std::cout << "FOO not defined\n";
#endif
}