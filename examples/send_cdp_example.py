"""Simple example script using scapy-cdp to send CDP packets."""

from scapy_cdp.cdp_sender import send_cdp_packet


if __name__ == "__main__":
    # Adjust the parameters below as needed for your environment.
    send_cdp_packet(
        interface="eth0",
        device_id="MyDevice",
        software_version="1.2.3",
        platform="MyPlatform",
        ttl=120,
        capabilities=0x0038,
    )
