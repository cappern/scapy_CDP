#!/usr/bin/env python3
import time
from scapy.all import *
from scapy.layers.l2 import CDPMsgDeviceID, CDPMsgSoftwareVersion

def send_cdp():
    iface = "eth0"  # Endre hvis nødvendig
    while True:
        cdp_pkt = Ether(dst="01:00:0c:cc:cc:cc") / \
                  CDPMsgDeviceID(val="Kali-Linux") / \
                  CDPMsgSoftwareVersion(val="Kali 2024")

        sendp(cdp_pkt, iface=iface, verbose=False)
        print("CDP packet sent")
        time.sleep(60)  # Vent 60 sekunder

if __name__ == "__main__":
    send_cdp()
