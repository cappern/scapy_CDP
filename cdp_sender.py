from scapy.all import *
from scapy.layers.l2 import Ether, SNAP, LLC
from scapy.contrib.cdp import (CDPv2_HDR, CDPMsgDeviceID, CDPMsgPortID, 
                              CDPMsgSoftwareVersion, CDPMsgPlatform, CDPMsgAddr,
                              CDPAddrRecordIPv4, CDPMsgCapabilities)
import time

def send_cdp_packet(interface):
    # Get the MAC address and IP of the interface
    src_mac = get_if_hwaddr(interface)
    src_ip = get_if_addr(interface)
    print(f"Using source MAC address: {src_mac}")
    print(f"Using source IP address: {src_ip}")
    
    # Create base packet with CDP multicast address and correct source MAC
    eth = Ether(dst='01:00:0c:cc:cc:cc', src=src_mac)
    llc = LLC(dsap=0xaa, ssap=0xaa, ctrl=3)
    snap = SNAP(OUI=0x00000c, code=0x2000)
    
    # Create the address record
    addr_record = CDPAddrRecordIPv4(addr=src_ip)
    
    cdp = CDPv2_HDR(
        ttl=180,  # 180 seconds TTL
        msg=[
            CDPMsgDeviceID(val='Cisco_AP_01'),
            CDPMsgAddr(
                naddr=1,
                addr=[addr_record]
            ),
            CDPMsgCapabilities(
                cap=0x0028    # Set capabilities for AP (0x0028 = Host + IGMP capabilities)
            ),
            CDPMsgSoftwareVersion(val='AP Software 8.5.1'),
            CDPMsgPlatform(val='Cisco Aironet 2800'),
            CDPMsgPortID(iface=interface)
        ]
    )
    
    packet = eth/llc/snap/cdp
    
    try:
        while True:
            sendp(packet, iface=interface, verbose=False)
            print(f"CDP packet sent on interface {interface} at {time.strftime('%H:%M:%S')}")
            time.sleep(60)  # Wait 60 seconds before next packet
    except KeyboardInterrupt:
        print("\nStopping CDP sender...")
    except Exception as e:
        print(f"Error sending packet: {e}")

if __name__ == "__main__":
    # List available interfaces
    print("Available interfaces:")
    print(get_if_list())
    
    interface = "eth0"  # Change to your interface
    print(f"Starting CDP sender on {interface}")
    print("Press Ctrl+C to stop")
    send_cdp_packet(interface)
