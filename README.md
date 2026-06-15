# Network Recon Toolkit

A Python and Bash-based Network Reconnaissance Toolkit designed to perform host discovery, network information gathering, and port enumeration. This project demonstrates practical networking, security automation, and reconnaissance concepts commonly used by cybersecurity professionals during security assessments and investigations.

## Project Overview

Network reconnaissance is a critical phase of cybersecurity operations. Security professionals use reconnaissance techniques to identify active hosts, discover exposed services, understand network environments, and support security assessments.

This project combines Python and Bash scripting to automate common reconnaissance tasks and strengthen practical skills in networking, security operations, and system administration.

## Features

### Python Network Scanner

* Scans common TCP ports
* Detects open ports
* Identifies common network services
* Performs basic host enumeration
* Generates scan results for analysis

### Bash Reconnaissance Script

* Collects host information
* Displays current user information
* Retrieves IP address configuration
* Displays routing information
* Lists active network connections
* Automates basic reconnaissance tasks

## Technologies Used

* Python
* Bash
* Socket Programming
* Linux Networking Commands
* TCP/IP Fundamentals
* Git
* GitHub

## Project Structure

```text
network-recon-toolkit/
│
├── network_scanner.py
├── network_recon.sh
├── README.md
├── requirements.txt
└── Screenshots/
```

## How It Works

### Python Scanner

The scanner prompts the user for a target IP address and checks common TCP ports for open services.

Example scanned ports:

* FTP (21)
* SSH (22)
* SMTP (25)
* DNS (53)
* HTTP (80)
* POP3 (110)
* Microsoft RPC (135)
* NetBIOS (139)
* HTTPS (443)
* SMB (445)
* RDP (3389)

### Bash Recon Script

The Bash script gathers local system and network information including:

* Hostname
* Current user
* IP configuration
* Routing table
* Active network connections

## Sample Output

```text
==================================================
NETWORK RECON TOOLKIT
==================================================

Scanning 127.0.0.1...

[OPEN] Port 135 (Microsoft RPC)
[OPEN] Port 445 (SMB)

==================================================
Total Open Ports: 2
Scan Complete
==================================================
```

## Security Use Cases

* Network Discovery
* Host Enumeration
* Port Enumeration
* Security Assessments
* Security Operations
* Incident Investigation
* Threat Hunting Preparation

## Learning Outcomes

Through this project, I gained hands-on experience with:

* TCP/IP Networking
* Port Scanning Concepts
* Service Identification
* Bash Scripting
* Python Automation
* Network Enumeration
* Security Reconnaissance Techniques

## Future Improvements

* Multi-host scanning
* Network range scanning
* Service banner grabbing
* CSV reporting
* Scan result logging
* Vulnerability lookup integration
* Real-time monitoring capabilities

## Project Screenshot

Add your scanner output screenshot inside the `Screenshots` folder and update the filename below if necessary.

```markdown
![Network Recon Toolkit Output](Screenshots/network-scanner-output.png)
```

## Author

**Gideon Nwachukwu (Paxvirs)**


