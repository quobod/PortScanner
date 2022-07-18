#! /usr/bin/python3

import socket  # for connecting
from threading import Thread, Lock
from queue import Queue
from custom_modules.ConsoleMessenger import CONSOLE_MESSENGER_SWITCH as cms

N_THREADS = 200
# thread queue
q = Queue()
print_lock = Lock()
host = ""


def port_scan(port):
    """
    determine whether `host` has the `port` open
    """
    # creates a new socket
    s = socket.socket()
    try:
        # tries to connect to host using that port
        s.connect(
            (
                host,
                port,
            )
        )
        # make timeout if you want it a little faster ( less accuracy )
        s.settimeout(0.2)
    except:
        with print_lock:
            cus = cms["custom"]
            msg = "Port {} is closed".format(port)
            cmsg = cus(100, 100, 100, msg)
            print("{}".format(cmsg))
    else:
        with print_lock:
            suc = cms["success"]
            msg = "Port {} is opened".format(port)
            smsg = suc(msg)
            print("{}".format(smsg))
    finally:
        s.close()


def scan_thread():
    global q
    while True:
        # get the port number from the queue
        worker = q.get()
        # scan that port number
        port_scan(worker)
        # tells the queue that the scanning for that port
        # is done
        q.task_done()


def start(h, ports):
    print(" " * 55 + "Threaded Port Scanner")
    global q
    global host
    for t in range(N_THREADS):
        # for each thread, start it
        t = Thread(target=scan_thread)
        # when we set daemon to true, that thread will end when the main thread ends
        t.daemon = True
        # start the daemon thread
        t.start()
    for worker in ports:
        # for each port, put that port into the queue
        # to start scanning
        q.put(worker)
    # wait the threads ( port scanners ) to finish
    q.join()
    host = h
