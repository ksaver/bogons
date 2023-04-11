#!/usr/bin/env python3
#
# Script to check if IP addresses are local (bogons) or public. 
#
# Run script with no arguments to see help.
#
# More info:
# https://simple.wikipedia.org/wiki/Bogon_filtering
# 

import argparse
import ipaddress
import os
import sys

bogons = ["0.0.0.0/8",
        "10.0.0.0/8",
        "100.64.0.0/10",
        "127.0.0.0/8",
        "127.0.53.53",
        "169.254.0.0/16",
        "172.16.0.0/12",
        "192.0.0.0/24",
        "192.0.2.0/24",
        "192.168.0.0/16",
        "198.18.0.0/15",
        "198.51.100.0/24",
        "203.0.113.0/24",
        "224.0.0.0/4",
        "240.0.0.0/4",
        "255.255.255.255/32",
        "::/128",
        "::1/128",
        "::ffff:0:0/96",
        "::/96",
        "100::/64",
        "2001:10::/28",
        "2001:db8::/32",
        "fc00::/7",
        "fe80::/10",
        "fec0::/10",
        "ff00::/8",
        "2002::/24",
        "2002:a00::/24",
        "2002:7f00::/24",
        "2002:a9fe::/32",
        "2002:ac10::/28",
        "2002:c000::/40",
        "2002:c000:200::/40",
        "2002:c0a8::/32",
        "2002:c612::/31",
        "2002:c633:6400::/40",
        "2002:cb00:7100::/40",
        "2002:e000::/20",
        "2002:f000::/20",
        "2002:ffff:ffff::/48",
        "2001::/40",
        "2001:0:a00::/40",
        "2001:0:7f00::/40",
        "2001:0:a9fe::/48",
        "2001:0:ac10::/44",
        "2001:0:c000::/56",
        "2001:0:c000:200::/56",
        "2001:0:c0a8::/48",
        "2001:0:c612::/47",
        "2001:0:c633:6400::/56",
        "2001:0:cb00:7100::/56",
        "2001:0:e000::/36",
        "2001:0:f000::/36",
        "2001:0:ffff:ffff::/64"]


def bogon_ipaddr(ipaddr):
    """Detect bogon IP addresses."""
    for bogon in bogons:
        net = ipaddress.ip_network(bogon)
        if ipaddress.ip_address(ipaddr) in net:
            return True # bogon detected

    return False


def parseargs(args):
    parser = argparse.ArgumentParser(
        description='Check if an IP address or a file with IP addresses are locals (bogons) or public IP addresses.'
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '-a', '--address', type=str,
        help='One IP Address to check.'
    )
    group.add_argument(
        '-f', '--file', type=str,
        help='File with a list of IP addresses.'
    )

    group2 = parser.add_mutually_exclusive_group(required=False)
    group2.add_argument(
        '--only-local', action='store_true',
        help='Show Local (Bogon) IP addresses only.'
    )
    group2.add_argument(
        '--only-public', action='store_true',
        help='Show Public IP addresses only.'
    )

    return parser.parse_args()


def main():

    arguments = parseargs(sys.argv)
    
    if arguments.address:
        ip_address = arguments.address
        if bogon_ipaddr(ip_address):
            print(f"Bogon: {ip_address}")
        else:
            print(f"Public: {ip_address}")

    elif arguments.file:
        with open(arguments.file) as f:
            for line in f:
                ip_address = line.strip()
                if arguments.only_public:
                    if not bogon_ipaddr(ip_address):
                        print(f"{ip_address}")
                elif arguments.only_local:
                    if bogon_ipaddr(ip_address):
                        print(f"{ip_address}")
                else:
                    if bogon_ipaddr(ip_address):
                        print(f"Bogon: {ip_address}")
                    else:
                        print(f"Public: {ip_address}")


if __name__ == '__main__':
    main()
