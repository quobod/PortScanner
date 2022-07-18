#! /usr/bin/python3

import socket  # for connecting
from ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms


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
                        print("\t{}".format(ex.args[1]))
                    elif len(ex.args) == 1:
                        print("\t{}".format(ex.args[0]))
                else:
                    print("\t{}".format(ex))

            return False
    return True


def check_port(host, port_start_range, port_end_range, verbose=False, timeout=None):
    _host = None
    sport = None
    eport = None
    _timeout = None

    if not timeout == None and not timeout <= 0:
        _timeout = timeout

    print(" " * 55 + "Port Scanner\n" + "-" * 12 + "> Target: {}".format(host))

    if not host == None and not len(host) == 0:
        _host = host

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

    if not _host == None:
        if sport and eport:
            for port in range(sport, eport):
                if verbose:
                    cus = cms["custom"]
                    msg = "\n\nChecking port {}".format(port)
                    vmsg = cus(222, 222, 222, msg)
                    print("{}".format(vmsg))

                    if is_port_open(_host, port, verbose, _timeout):
                        suc = cms["success"]
                        msg = "Port {} is opened".format(port)
                        smsg = suc(msg)
                        print("{}".format(smsg))
                    else:
                        cus = cms["custom"]
                        msg = "Port {} is closed".format(port)
                        cmsg = cus(100, 100, 100, msg)
                        print("{}".format(cmsg))
                else:
                    if is_port_open(_host, port, verbose):
                        suc = cms["success"]
                        msg = "Port {} is opened".format(port)
                        smsg = suc(msg)
                        print("{}".format(smsg))
        elif sport and not eport:
            if verbose:
                cus = cms["custom"]
                msg = "\n\nChecking port {}".format(sport)
                vmsg = cus(222, 222, 222, msg)
                print("{}".format(vmsg))

                if is_port_open(_host, sport, verbose, _timeout):
                    suc = cms["success"]
                    msg = "Port {} is opened".format(sport)
                    smsg = suc(msg)
                    print("{}".format(smsg))
                else:
                    cus = cms["custom"]
                    msg = "Port {} is closed".format(sport)
                    cmsg = cus(100, 100, 100, msg)
                    print("{}".format(cmsg))
            else:
                if is_port_open(_host, sport, verbose, _timeout):
                    suc = cms["success"]
                    msg = "Port {} is opened".format(sport)
                    smsg = suc(msg)
                    print("{}".format(smsg))
