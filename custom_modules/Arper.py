#! /usr/bin/python3

from scapy.all import *
import re
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms
from custom_modules.ArgumentManager import filtered, filtered_count
from custom_modules.PatternConstants import IP4


def make_arp_request(
    _network_target="192.168.1.1/24", destination="ff:ff:ff:ff:ff:ff", verbosity=False
):
    network_target = "192.168.1.1/24"
    _dst = "ff:ff:ff:ff:ff:ff"
    verbose = False

    if not _network_target == None:
        network_target = _network_target

    if not destination == None:
        _dst = destination

    if not verbosity == None:
        verbose = verbosity

    ip = IP()
    arp = ARP(pdst=network_target)
    ether = Ether(dst=_dst)
    packet = ether / arp

    result = srp(packet, timeout=3)[0]

    clients = []

    for sent, received in result:
        received.show_summary = True
        ip_address = None
        my_dict = {}

        _search = re.search(IP4, received.summary())

        if not _search == None:
            my_dict.update(
                {
                    "ip": _search.group(),
                    "mac": received.src,
                }
            )
        else:
            my_dict.update(
                {
                    "mac_src": received.src,
                    "mac_dst": received.dst,
                }
            )

        clients.append(my_dict)

    if verbose:
        print("\n\nAvailable devices in the network:")
        print("IP" + "  " * 18 + "MAC\n" + "-" * 55)
        for client in clients:
            print("{:16}                      {}".format(client["ip"], client["mac"]))
