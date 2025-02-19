from scapy.all import *
from scapy.layers.l2 import Ether, SNAP, LLC
from scapy.contrib.cdp import CDPv2_HDR, CDPMsgDeviceID, CDPMsgPortID, CDPMsgSoftwareVersion, CDPMsgPlatform
import time

def send_cdp_packet(interface):
    # Create base packet with CDP multicast address
    eth = Ether(dst='01:00:0c:cc:cc:cc')
    llc = LLC(dsap=0xaa, ssap=0xaa, ctrl=3)
    snap = SNAP(OUI=0x00000c, code=0x2000)
    
    cdp = CDPv2_HDR(
        ttl=180,  # 180 seconds TTL
        msg=[
            CDPMsgDeviceID(val='Python_AP_01'),
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
    interface = "eth0"  # Change to your interface
    print(f"Starting CDP sender on {interface}")
    print("Press Ctrl+C to stop")
    send_cdp_packet(interface)
