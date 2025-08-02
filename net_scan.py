#!/usr/bin/env python3

import socket
import argparse
from termcolor import colored
import sys

def get_parameters():
    parser = argparse.ArgumentParser(description="Un escaner de red TCP.")
    parser.add_argument("--host", "-H", dest="host", help="Direccion IP a escanear (Ex: python3 net_scan.py -H 192.168.1.1)")
    parser.add_argument("--ports", "-p", dest="ports", help="Puertos a escanear (Ex: -p 20-100 or -p 22 or -p 22,80,443)")
    args = parser.parse_args()

    if not args.host or not args.ports:
        parser.print_help()
        sys.exit(1)

    return args.host, args.ports

def create_socket():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.2)
    return s

def connection_attempt(host, port, s):

    try:
        s.connect((host, port))
        print(colored(f"Puerto {port} - status [Abierto]", 'green'))
        s.close()

    except (socket.timeout, ConnectionRefusedError):
        s.close()

def main():

    host, port_str = get_parameters()

    if "-" in port_str:
        inicio, final = map(int, port_str.split("-"))

        print()
        for port in range(inicio, final+1):
            s = create_socket()
            connection_attempt(host, port, s)

    elif "," in port_str:
        ports = port_str.split(",")

        print()
        for port in ports:
            s = create_socket()
            connection_attempt(host, int(port), s)

    else:
        s = create_socket()
        connection_attempt(host, int(port_str), s)

if __name__ == '__main__':
    main()
