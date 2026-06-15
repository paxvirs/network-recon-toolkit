import socket

target = input("Enter target IP: ")

ports = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    135: "Microsoft RPC",
    139: "NetBIOS",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP"
}

print("=" * 50)
print("NETWORK RECON TOOLKIT")
print("=" * 50)

print(f"\nScanning {target}...\n")

open_ports = 0

for port, service in ports.items():

    scanner = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    scanner.settimeout(1)

    result = scanner.connect_ex(
        (target, port)
    )

    if result == 0:

        print(
            f"[OPEN] Port {port} ({service})"
        )

        open_ports += 1

    scanner.close()

print("\n" + "=" * 50)
print(f"Total Open Ports: {open_ports}")
print("Scan Complete")
print("=" * 50)