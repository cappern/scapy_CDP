# CDP Sender Script Instructions

## Overview
This guide explains how to set up and use a CDP (Cisco Discovery Protocol) sender script on Kali Linux. The script uses **Scapy** to send CDP packets every 60 seconds.

## Prerequisites
Ensure you have the following installed:

- Python 3
- Scapy
- Systemd (for automatic startup)

### Install Scapy (if not installed)
```bash
sudo apt update
sudo apt install python3-scapy -y
```

## Script Location
The script should be stored at:
```bash
/usr/local/bin/cdp_sender.py
```

### Grant Execution Permission
```bash
sudo chmod +x /usr/local/bin/cdp_sender.py
```

## Running the Script Manually
To manually start the script, run:
```bash
sudo /usr/local/bin/cdp_sender.py
```

## Setting Up Automatic Execution with systemd
To ensure the script starts at boot and runs continuously, follow these steps:

### 1. Create a Systemd Service File
Create the service file:
```bash
sudo nano /etc/systemd/system/cdp_sender.service
```

### 2. Add the Following Content
```ini
[Unit]
Description=CDP Sender Service
After=network.target

[Service]
ExecStart=/usr/local/bin/cdp_sender.py
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

Save and exit (`CTRL+X`, `Y`, `Enter`).

### 3. Enable and Start the Service
Reload systemd and enable the service:
```bash
sudo systemctl daemon-reload
sudo systemctl enable cdp_sender
sudo systemctl start cdp_sender
```

### 4. Check Service Status
To verify that the service is running:
```bash
sudo systemctl status cdp_sender
```

## Logs and Debugging
To check real-time logs:
```bash
journalctl -u cdp_sender -f
```

To restart the service:
```bash
sudo systemctl restart cdp_sender
```

To stop the service:
```bash
sudo systemctl stop cdp_sender
```

## Alternative: Using Cron
If you prefer to use cron instead of systemd, add the following entry:
```bash
sudo crontab -e
```
Add this line at the end:
```bash
* * * * * /usr/local/bin/cdp_sender.py
```
This will run the script every minute.

## Conclusion
By following these steps, Kali Linux will automatically send CDP packets every 60 seconds. You can choose between **systemd** for continuous execution or **cron** for periodic execution.

Enjoy your CDP sender automation! 🚀

