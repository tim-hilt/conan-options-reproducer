#include <iostream>
#include "webserver.hpp"
#include "3rdparty.hpp"
#include "tcp_ip.hpp"

void callPrintFoo()
{
    printFoo();
    tcpIpStuff();
}
