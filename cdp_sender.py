from scapy.all import *
from scapy.contrib.cdp import CDP, CDPMsgDeviceID, CDPMsgSoftwareVersion
from scapy.contrib.cdp import CDPMsgPlatform, CDPMsgPortID

def send_cdp_packet(interface):
    # Create Ethernet header (CDP uses multicast address)
    eth = Ether(dst='01:00:0c:cc:cc:cc', type=0x011e)
    
    # Create LLC header
    llc = LLC(dsap=0xaa, ssap=0xaa, ctrl=3)
    snap = SNAP(OUI=0x00000c, code=0x2000)
    
    # Create CDP packet with device information
    cdp = CDP(
        vers=2,
        ttl=180,
        msg=[
            CDPMsgDeviceID(val='Python_AP_01'),
            CDPMsgSoftwareVersion(val='AP Software 8.5.1'),
            CDPMsgPlatform(val='Cisco Aironet 2800'),
            CDPMsgPortID(val=interface)
        ]
    )
    
    # Combine all layers
    packet = eth/llc/snap/cdp
    
    # Send the packet
    try:
        sendp(packet, iface=interface)
        print(f"CDP packet sent on interface {interface}")
    except Exception as e:
        print(f"Error sending packet: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with your network interface
    interface = "eth0"
    send_cdp_packet(interface)
