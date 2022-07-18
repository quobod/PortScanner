#! /usr/bin/python3

_set = set()
f = open("sudo_nmap_-sU_-O_192.168.1.0_24_results.txt")

for x in f:
    _set.add(x)

print(*_set,sep="\n")