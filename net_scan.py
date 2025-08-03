#!/usr/bin/env python3

try:
    from termcolor import colored
except ImportError:
    print(f"\n[!] Falta la librería 'termcolor'.\nEjecuta: pip install -r requirements.txt")
    exit(1)

import socket
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_parameters():
    parser = argparse.ArgumentParser(description="Un escaner de red TCP.")
    parser.add_argument("--host", "-H", dest="host", required=True, help="Direccion IP a escanear (Ex: python3 net_scan.py -H 192.168.1.1)")
    parser.add_argument("--ports", "-p", dest="ports", required=True, help="Puertos a escanear (Ex: -p 20-100 o -p 22 o -p 22,80,443)")
    args = parser.parse_args()

    return args.host, args.ports

def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.2)
    return s

def connection_attempt(host, port):

    s = create_socket()

    try:
        # Operacion Entrada/Salida E/S -> Utilizar hilos para mayor rapidez
        s.connect((host, port))
        return port
    except (socket.timeout, ConnectionRefusedError):
        return None
    finally:
        s.close()

def port_iterator(ports, host):
    # Excesivo consumo de recursos con Threading, limitar uso de hilos con ThreadPoolExcecutor
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(connection_attempt, host, port) for port in ports]

        results = []

        for future in as_completed(futures):
            result = future.result()
            if result:
                results.append(result)

    for port in sorted(results):
        print(colored(f"Puerto {port} - status [Abierto]", 'green'))

def port_parser(port_str):

    if "-" in port_str:
        inicio, final = map(int, port_str.split("-"))
        return range(inicio, final+1)
    elif "," in port_str:
        return map(int, port_str.split(","))
    else:
        return [int(port_str)]

def main():

    host, port_str = get_parameters()
    ports = port_parser(port_str)
    print(colored(f"\n[+] Escaneando puertos...\n", 'cyan'))
    port_iterator(ports, host)

if __name__ == '__main__':
    main()
