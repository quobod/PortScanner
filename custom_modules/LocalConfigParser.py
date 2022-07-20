#! /usr/bin/python3

from scapy.all import *

""" 
    Returns local network interface name
    It's IP address and the gateway address
"""


def return_route():
    return (
        conf.route.route("0.0.0.0")[0],
        conf.route.route("0.0.0.0")[1],
        conf.route.route("0.0.0.0")[2],
    )
