#! /usr/bin/python3

import argparse
import re
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from custom_modules.PatternConstants import IP4, IPv4
from custom_modules.LocalConfigParser import (
    return_arp_results,
    return_gateway_addr,
    return_local_ip_address,
    return_local_ip_address_by_name,
    return_local_mac_address,
    return_local_mac_address_by_iface_name,
    return_local_route,
    return_mac_by_ip_address,
    return_route,
)

desc = "A network information gathering tool"
if_name, if_addr, gateway = return_route()
cus = cms["custom"]
msg = None
match = None

parser = argparse.ArgumentParser(description=desc)

""" group optional arguments """

group = parser.add_mutually_exclusive_group()

group.add_argument(
    "-v", "--verbose", help="Increase output verbosity", action="count", default=0
)

""" positional arguments """

parser.add_argument(
    "-a",
    "--arp",
    help="Make arp request for hosts on given network; e.g. --arp 110.2.77.43/72.",
    default=gateway,
)

# parse arguments
args = parser.parse_args()

""" ARP Request  """

if not args.arp:
    args.arp = gateway

if args.verbose >= 2:
    msg = "Running program with level {} verbosity".format(args.verbose)
    cmsg = cus(255, 235, 195, msg)
    print(cmsg)

    match = re.search(IP4, args.arp)

    if not match == None:
        msg = "Making arp request to target {}".format(args.arp)
        cmsg = cus(255, 255, 255, msg)
        print(cmsg)
        cmsg = cus(137, 223, 137, "")
        print(cmsg)
        ans, unans = return_arp_results(args.arp)
        # ans.nsummary()
        # print(ans)
    else:
        msg = "Address {} is invalid\nExpecting a valid IP4 or IP6 address.".format(
            args.arp
        )
        cmsg = cus(223, 87, 87, msg)
        print(cmsg)
else:
    match = re.search(IPv4, args.arp)

    if not match == None:
        # msg = "Making arp request to target {}".format(args.arp)
        # cmsg = cus(127, 253, 127, msg)
        # print(cmsg)
        ans, unans = return_arp_results(args.arp)
        # ans.nsummary()
        # print(ans)
    else:
        msg = "Address {} is invalid\nExpecting a valid IP4 or IP6 address.".format(
            args.arp
        )
        cmsg = cus(223, 87, 87, msg)
        print(cmsg)
