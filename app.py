#! /usr/bin/python3
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *


import threading
import time
from custom_modules.ArgumentManager import filtered, filtered_count
from custom_modules.PortScanner import check_port as chp
from custom_modules.LocalConfigParser import (
    return_route as rr,
    return_local_route as rlr,
    return_arp_results as rar,
    return_gateway_addr,
    return_local_ip_address,
    return_local_mac_address,
    return_mac_by_ip_address,
)


def test_port_scanner():
    if filtered_count == 3:
        host = filtered[0]
        sport = int(filtered[1])
        eport = int(filtered[2])
        ports = (sport, eport)
        chp(host, ports, None, None, None)

    elif filtered_count == 4:
        host = filtered[0]
        sport = int(filtered[1])
        eport = int(filtered[2])
        ports = (sport, eport)
        verbose = bool(filtered[3])
        chp(host, ports, None, verbose)
    else:
        print("{}".format("No arguments"))


# print("Local MAC by IP address:\t{}".format(return_mac_by_ip_address("192.168.1.71")))

# print(type(return_local_ip_address()))

test_port_scanner()
