#! /usr/bin/python3

import argparse
import re
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from custom_modules.PatternConstants import IP4, IPv4, IPv4_network
from custom_modules.LocalConfigParser import (
    return_arp_results as rar,
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
epil = "Make ARP requests to given host or network range"
if_name, if_addr, gateway = return_route()
cus = cms["custom"]
msg = None
match = None


parser = argparse.ArgumentParser(description=desc, epilog=epil)

""" group optional arguments """

group = parser.add_mutually_exclusive_group()

# Increase verbosity
group.add_argument(
    "-v",
    "--verbose",
    dest="verbose",
    action="store_true",
    help="Increase output verbosity",
)

group.add_argument(
    "-q", "--quiet", dest="verbose", action="store_false", help="Silently run program"
)

""" positional arguments """

# Run program
parser.add_argument(
    "-a",
    "--arp",
    help="Make arp request for hosts on given network; e.g. --arp 110.2.77.43/72.",
)

# Set timeout
parser.add_argument(
    "-t", "--timeout", help="Set the number of seconds to give up", type=int
)

# Update system cache
parser.add_argument(
    "-c",
    "--cache",
    choices=["yes", "no"],
    help="Whether or not to refresh system's arp cache - e.g. 0 = True, 1 = False",
)

# Print report
parser.add_argument(
    "-r", "--report", choices=["yes", "no"], help="Print results to a text file"
)

# parse arguments
args = parser.parse_args()

""" ARP Request  """

_target = "{}/24".format(gateway)
_timeout = None
_cache = None
_verbose = None
_report = None

if args.arp:
    _target = args.arp

if args.timeout:
    _timeout = args.timeout

if args.verbose:
    _verbose = True
else:
    _verbose = False

if args.cache:
    if args.cache.lower().strip() == "yes":
        _cache = True
    else:
        _cache = False

if args.report:
    if args.report.lower().strip() == "yes":
        _report = True
    else:
        _report = False

print("Target,  Timeout,  Cache,  Verbose,  Report")
print("{}  {}  {}  {}  {}".format(_target, _timeout, _cache, _verbose, _report))

rar(_target, _timeout, _cache, _verbose, _report)
