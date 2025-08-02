#!/usr/bin/env python3

import socket
from termcolor import colored

host = input("[+] Ingresa una direccion IP: ")

def create_socket():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    return s

def connection_attempt(host, port, s):

    try:
        s.connect((host, port))
        print(colored(f"\n[+] El puerto {port} está abierto", 'green'))
        s.close()

    except (socket.timeout, ConnectionRefusedError):
        s.close()

def main():

    for port in range(1, 1000):
        s = create_socket()
        connection_attempt(host, port, s)

if __name__ == '__main__':
    main()
