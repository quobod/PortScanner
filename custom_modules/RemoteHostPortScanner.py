#! /usr/bin/python3

import argparse
from ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from PortScanner import check_port as chp


cus = cms["custom"]
msg = None
timeout = None
port_range = False
sport = 1
eport = 65534
ports = range(sport, eport)
host = "192.168.1.1"

parser = argparse.ArgumentParser(description="Remote host port scanner")

group = parser.add_mutually_exclusive_group()

# group arguments
group.add_argument(
    "-v", "--verbose", help="Increase output verbosity", action="count", default=0
)
group.add_argument(
    "-q", "--quiet", help="Silently run the program", action="store_true"
)

# positional arguments
parser.add_argument(
    "-a",
    "--addr",
    help="The host IP address",
    default="192.168.1.1",
)

parser.add_argument(
    "-t",
    "--timeout",
    type=float,
    help="Set connection time out in seconds - e.g. 0.2 or 10.",
)

parser.add_argument(
    "-p",
    "--ports",
    help="Select which port or range of ports to scan; e.g. -p 22 or -p 1-1024. Defaults from 1 to 65,534",
    default="{}-{}".format(sport, eport),
)

args = parser.parse_args()

# Quiet mode
if args.quiet:
    msg = "Run program silently"
    cmsg = cus(177, 200, 177, msg)
    print("\n\t\t\t{}\n".format(cmsg) + "-" * 75 + "\n")

    if args.addr:
        host = args.addr

    if args.timeout:
        timeout = args.timeout

    if args.ports:
        if "-" in args.ports:
            ports_split = args.ports.split("-")
            sport = int(ports_split[0])
            eport = int(ports_split[1])
            port_range = True
        else:
            sport = int(args.ports)

    if port_range:
        print("Scanning host {}'s ports {} - {}".format(host, sport, eport))
        chp(host, sport, eport, False, timeout)

    else:
        print("Scanning host {}'s port {}".format(host, sport))
        chp(host, sport, None, False, timeout)

# Level 2 verbose mode
elif args.verbose >= 2:
    msg = "Running program with level {} verbosity".format(args.verbose)
    cmsg = cus(177, 230, 177, msg)
    print("\n\t\t\t{}\n".format(cmsg) + "-" * 75 + "\n")

    if args.addr:
        host = args.addr

    if args.timeout:
        timeout = args.timeout

    if args.ports:
        if "-" in args.ports:
            ports_split = args.ports.split("-")
            sport = int(ports_split[0])
            eport = int(ports_split[1])
            port_range = True
        else:
            sport = int(args.ports)

    if port_range:
        print("Scanning host {}'s ports {} - {}".format(host, sport, eport))
        chp(host, sport, eport, True, timeout)
    else:
        print("Scanning host {}'s port {}".format(host, sport))
        chp(host, sport, None, True, timeout)

# Level 1 verbose mode
elif args.verbose >= 1:
    msg = "Running program with level {} verbosity".format(args.verbose)
    cmsg = cus(177, 240, 177, msg)
    print("\n\t\t\t{}\n".format(cmsg) + "-" * 75 + "\n")

    if args.addr:
        host = args.addr

    if args.timeout:
        timeout = args.timeout

    if args.ports:
        if "-" in args.ports:
            ports_split = args.ports.split("-")
            sport = int(ports_split[0])
            eport = int(ports_split[1])
            port_range = True
        else:
            sport = int(args.ports)

    if port_range:
        print("Scanning host {}'s ports {} - {}".format(host, sport, eport))
        chp(host, sport, eport, True, timeout)
    else:
        print("Scanning host {}'s port {}".format(host, sport))
        chp(host, sport, None, True, timeout)
else:
    msg = "Run program with default config"
    cmsg = cus(177, 200, 177, msg)
    print("\n\t\t\t{}\n".format(cmsg) + "-" * 75 + "\n")

    if args.addr:
        host = args.addr

    if args.timeout:
        timeout = args.timeout

    if args.ports:
        if "-" in args.ports:
            ports_split = args.ports.split("-")
            sport = int(ports_split[0])
            eport = int(ports_split[1])
            port_range = True
        else:
            sport = int(args.ports)

    if port_range:
        print("Scanning host {}'s ports {} - {}".format(host, sport, eport))
        chp(host, sport, eport, False, timeout)
    else:
        print("Scanning host {}'s port {}".format(host, sport))
        chp(host, sport, None, False, timeout)
