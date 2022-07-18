#! /usr/bin/python3
import re
from custom_modules.PatternConstants import IP4 as ip4_pattern


def print_to_console():
    _set = set()
    f = open("sudo_nmap_-sU_-O_192.168.1.0_24_results.txt", mode="r")

    for x in f:
        src = re.search(ip4_pattern, x)
        if not src == None:
            _set.add(src.group())
    f.close()

    print(*_set, sep="\n")


def print_to_set():
    _set = set()
    f = open("sudo_nmap_-sU_-O_192.168.1.0_24_results.txt")

    for x in f:
        src = re.search(ip4_pattern, x)
        if not src == None:
            _set.add(src.group())
    f.close()

    count = len(_set)
    return count, _set


def print_to_list():
    _set = set()
    _list = []

    f = open("sudo_nmap_-sU_-O_192.168.1.0_24_results.txt")

    for x in f:
        src = re.search(ip4_pattern, x)
        if not src == None:
            _set.add(src.group())
    f.close()

    for s in _set:
        _list.append(s)

    count = len(_list)
    return count, _list


def populate_list(l_arg):
    _set = set()

    if not l_arg == None:
        if type(l_arg) == list:
            l_arg.clear()
        else:
            l_arg = []
    else:
        l_arg = []

    f = open("sudo_nmap_-sU_-O_192.168.1.0_24_results.txt")

    for x in f:
        src = re.search(ip4_pattern, x)
        if not src == None:
            _set.add(src.group())
    f.close()

    for s in _set:
        l_arg.append(s)

    count = len(l_arg)
    return count, l_arg
