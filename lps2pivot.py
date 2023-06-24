#!/usr/bin/python

import socket
import sys
import os
import argparse

print("W3lcome,", os.getlogin(),"!\n")

parser = argparse.ArgumentParser(description='Local Port Scan 2 Pivoting Script')

#Args
parser.add_argument('-H', '--host', type=str, help='Argument used to scan external networks.')
parser.add_argument('-P', '--port', type=int, help='Argument used to specify a single port.')

args = parser.parse_args()

host = args.host

if host is None:
    print("Keep patience and hack the planet...\n")
    for lport in range(1, 65535):
        lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lsock.settimeout(1)
        result = lsock.connect_ex(('localhost', lport))
        if result == 0:
            try:
                service_name = socket.getservbyport(lport)
            except OSError:
                service_name = "Unknown"
            print(f"PORT: {lport}, SERVICE: {service_name}, [OPEN]")
        lsock.close()
else:
    print("Keep patience and hack the planet...\n")
    for lport in range(1, 65535):
        lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lsock.settimeout(1)
        result = lsock.connect_ex((host, lport))
        if result == 0:
            try:
                service_name = socket.getservbyport(lport)
            except OSError:
                service_name = "Unknown"
            print(f"HOST: {host}, PORT: {lport}, SERVICE: {service_name}, [OPEN]")
        lsock.close()
