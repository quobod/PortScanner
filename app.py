#! /usr/bin/python3
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *


import threading
import time
from custom_modules.ArgumentManager import filtered, filtered_count
from custom_modules.PortScanner import check_port as chp

if filtered_count == 3:
    host = filtered[0]
    sport = int(filtered[1])
    eport = int(filtered[2])
    chp(host, sport, eport)

if filtered_count == 4:
    host = filtered[0]
    sport = int(filtered[1])
    eport = int(filtered[2])
    verbose = bool(filtered[3])
    chp(host, sport, eport, verbose)
