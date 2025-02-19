#!/usr/bin/env python3
import time
from scapy.all import *
from scapy.contrib.cdp import CDP, CDPTLV  # Ensure the CDP module is loaded

def send_cdp():
    iface = "eth0"  # Change this to match your network interface

    cdp_packet = (
        Ether(dst="01:00:0c:cc:cc:cc") /  # CDP uses this multicast address
        CDP(version=2, ttl=180) /  # CDP Header
        CDPTLV(type=1, value="Kali-Linux") /  # Device ID TLV
        CDPTLV(type=5, value="Kali 2024 Scapy Test")  # Software Version TLV
    )

    while True:
        sendp(cdp_packet, iface=iface, verbose=True)
        print("CDP packet sent on", iface)
        time.sleep(60)  # Send packet every 60 seconds

if __name__ == "__main__":
    send_cdp()
