#! /usr/bin/python3

from ast import Param
import socket

from paramiko import HostKeys  # for connecting
from .ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms


def is_port_open(host, port, verbose=False, timeout=None):
    _timeout = 2.2

    if not timeout == None and not timeout <= 0:
        _timeout = timeout

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.settimeout(_timeout)
            s.connect((host, port))
        except Exception as ex:
            if verbose:
                if "class" in str(type(ex)):
                    if len(ex.args) > 1:
                        print("{}".format(ex.args[1]))
                    elif len(ex.args) == 1:
                        print("{}".format(ex.args[0]))
                # else:
                #     print("{}".format(ex))

            return False
    return True


""" Method checks argument validity and run calls to the is_port_open method accordingly
    @Param host 
    @Param port_start_range 
    @Param port_end_range 
    @Param verbose 
    @Param timeout 
"""


def check_port(
    host=None, port_start_range=None, port_end_range=None, verbose=False, timeout=None
):
    _host = None
    sport = None
    eport = None
    _verbose = False
    _timeout = 2.2
    _port_range = False

    if not host == None and not len(host) == 0:
        _host = host

    if "<class 'tuple'>" == str(type(port_start_range)) and len(port_start_range) == 2:
        sport = port_start_range[0]
        eport = port_start_range[1]
        _port_range = True
    else:
        _port_range = False
        if (
            not port_end_range == None
            and not port_end_range <= 0
            and not len(str(port_end_range)) == 0
        ):
            eport = port_end_range

        if (
            not port_start_range == None
            and not port_start_range <= 0
            and not len(str(port_start_range)) == 0
        ):
            sport = port_start_range

    if not verbose == None and verbose:
        _verbose = verbose

    if not timeout == None and not timeout <= 0:
        _timeout = timeout

    if _verbose:
        print(" " * 55 + "Port Scanner\n" + "-" * 25 + "> Target: {}".format(host))

        if _port_range:
            for port in range(sport, eport):
                cus = cms["custom"]
                msg = "Checking port {}".format(port)
                cmsg = cus(222, 222, 222, msg)
                print("{}".format(cmsg))

                if is_port_open(_host, port, _verbose, _timeout):
                    suc = cms["success"]
                    msg = "Port {} is opened".format(port)
                    smsg = suc(msg)
                    print("{}\n".format(smsg))
                else:
                    cus = cms["custom"]
                    msg = "Port {} is closed".format(port)
                    cmsg = cus(100, 100, 100, msg)
                    print("{}\n".format(cmsg))
        else:
            if sport:
                if is_port_open(_host, sport, verbose, _timeout):
                    suc = cms["success"]
                    msg = "Port {} is opened".format(sport)
                    smsg = suc(msg)
                    print("{}\n".format(smsg))
                else:
                    cus = cms["custom"]
                    msg = "Port {} is closed".format(sport)
                    cmsg = cus(100, 100, 100, msg)
                    print("{}\n".format(cmsg))
    else:

        if _port_range:
            for port in range(sport, eport):
                if is_port_open(_host, port, _verbose, _timeout):
                    suc = cms["success"]
                    msg = "Port {} is opened".format(port)
                    smsg = suc(msg)
                    print("{}".format(smsg))
                else:
                    cus = cms["custom"]
                    msg = "Port {} is closed".format(port)
                    cmsg = cus(100, 100, 100, msg)
                    # print("{}".format(cmsg))
        else:
            if sport:
                if is_port_open(_host, sport, verbose, _timeout):
                    suc = cms["success"]
                    msg = "Port {} is opened".format(sport)
                    smsg = suc(msg)
                    print("{}".format(smsg))
                else:
                    cus = cms["custom"]
                    msg = "Port {} is closed".format(sport)
                    cmsg = cus(100, 100, 100, msg)
                    # print("{}".format(cmsg))
