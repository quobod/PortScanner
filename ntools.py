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
epil = "This program needs adminstrative access to perform many, if not, all of it's tasks."
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

# Run silently
group.add_argument(
    "-q", "--quiet", dest="verbose", action="store_false", help="Silently run program"
)

""" positional arguments """

# Print local routing table
parser.add_argument(
    "-l", "--local", action="store_true", dest="local", help="Print local routing table"
)

# Print gateway address
parser.add_argument(
    "-g", "--gateway", action="store_true", dest="gateway", help="Print gateway address"
)

# Run program
parser.add_argument(
    "-a",
    "--arp",
    help="ARP to host or network e.g. --arp 192.167.45.3 or --arp 10.1.10.1/8.",
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
    help="Whether or not to refresh system's arp cache - e.g. yes or no. Defaults to no",
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

# print("Target,  Timeout,  Cache,  Verbose,  Report")
# print("{}  {}  {}  {}  {}".format(_target, _timeout, _cache, _verbose, _report))

if _verbose:
    print(
        "ARPing Target: {}\tTimeout: {}\tCache? {}\tVerbose? {}\tReport? {}".format(
            _target, _timeout, _cache, _verbose, _report
        )
    )

rar(_target, _timeout, _cache, _verbose, _report)


""" Gateway Request  """

if args.gateway:
    gwa = return_gateway_addr()
    print("Gateway: {}".format(gwa))


""" Local Route Request  """


def print_local_route():
    msg = cms["custom"]
    local_route = return_route()
    dash = msg(245, 220, 199, "-")
    print(
        " {}".format(msg(255, 255, 255, "IFace"))
        + " " * 5
        + "\t  {}".format(msg(255, 255, 255, "Address"))
        + " " * 5
        + "\t\t {}".format(msg(255, 255, 255, "Gateway"))
    )
    print(dash * 29)
    print(*local_route, sep="\t\t")
    print("\n")


if args.local:
    print_local_route()
