#!/usr/bin/env python
#
# Checks if IP addresses are public or locals (Bogons)
#
# More info:
# https://simple.wikipedia.org/wiki/Bogon_filtering

import argparse
import ipaddress
import sys

def parse_args():
    parser = argparse.ArgumentParser(description='Check if IP addresses are public or bogons.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-a', '--address', help='Single IP address to check.')
    group.add_argument('-f', '--file', help='File containing a list of IP addresses to check.')
    group2 = parser.add_mutually_exclusive_group(required=False)
    group2.add_argument('--only-local', action='store_true', help='Show only local IP addresses.')
    group2.add_argument('--only-public', action='store_true', help='Show only public IP addresses.')
    args = parser.parse_args()
    return args


def is_valid_ip(ip_address):
    try:
        ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        return False


def is_bogon(ip_address):
    # if an IP address is not global, then it's a bogon,
    # also multicast ip addresses are considered bogons...
    ip = ipaddress.ip_address(ip_address)
    return ip.is_private or ip.is_multicast or ip.is_reserverd


def output_results(ip, args):
    if args.only_public or args.only_local:
        if not is_valid_ip(ip):
            return
    if args.only_public:
        if not is_bogon(ip):
            print(f"{ip}")
    elif args.only_local:
        if is_bogon(ip):
            print(f"{ip}")
    else:
        if not is_valid_ip(ip):
            print(f"Invalid IP address: '{ip}'")
            return
        if is_bogon(ip):
            print(f"Bogon: {ip}")
        else:
            print(f"Public: {ip}")


def main():
    args = parse_args()

    if args.address:
        # Add single IP address to list
        ip_addresses = [args.address]

    else:
        # Input standard input as file
        if args.file == '-':
            lines = sys.stdin.readlines()
        else:
            # Load list of IP addresses from a file
            with open(args.file) as f:
                lines = f.readlines()
        
        # Remove new line characters
        ip_addresses = [line.strip() for line in lines]

    for ip in ip_addresses:
        output_results(ip, args)


if __name__ == '__main__':
    main()

