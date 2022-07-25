#! /usr/bin/python3

import argparse
from ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms


cus = cms["custom"]
msg = None
sport = 1
eport = 65534
ports = range(sport, eport)


def error_handler(*args):
    cus = cms["custom"]
    arg = args[0]
    cargs = cus(254, 64, 4, arg)
    print("{}".format(cargs))


parser = argparse.ArgumentParser(description="Remote host port scanner")

parser.error = error_handler

group = parser.add_mutually_exclusive_group()

# group arguments
group.add_argument(
    "-v", "--verbose", help="Increase output verbosity", action="store_true"
)

group.add_argument(
    "-q", "--quiet", help="Silently run the program", action="store_true"
)

# positional arguments
parser.add_argument(
    "-s",
    "--scan",
    help="Scan port or range of ports. Options TCP or UDP, defaults to TCP.",
    choices=[
        "t",
        "tcp",
        "u",
        "udp",
    ],
    default="t",
)

args = parser.parse_args()

# print("Error: {}".format(parser))
