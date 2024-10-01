#include <iostream>
#include "3rdparty.hpp"

void printFoo()
{
#ifdef FOO
    std::cout << FOO << "\n";
#else
    std::cout << "FOO not defined\n";
#endif
}