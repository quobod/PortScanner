#! /usr/bin/python3

from scapy.all import *

""" 
    Returns local network interface name
    It's IP address and the gateway address
"""

IP = "0.0.0.0"

# Return 3 strings
def return_route():
    global IP
    return (
        conf.route.route(IP)[0],
        conf.route.route(IP)[1],
        conf.route.route(IP)[2],
    )


# Return tuple
def return_local_route():
    global IP
    return conf.route.route(IP)


# Arp request
def return_arp_results(mask="192.168.1.0/24", update_cache=True):
    return arping(mask, cache=update_cache)


# Get gateway address
def return_gateway_addr():
    return conf.route.route(get_if_addr(conf.iface[1]))[2]


# Get local IP address
def return_local_ip_address():
    return get_if_addr(conf.iface)


# Get local IP address by name
def return_local_ip_address_by_name(name=conf.iface):
    return get_if_addr(name)


# Get local MAC address
def return_local_mac_address():
    return get_if_hwaddr(conf.iface)


# Get local MAC address by iface name
def return_local_mac_address_by_iface_name(name=conf.iface):
    return get_if_hwaddr(name)


# Get MAC by IP address
def return_mac_by_ip_address(ip=get_if_addr(conf.iface)):
    return getmacbyip(ip)
