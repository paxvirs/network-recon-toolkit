#!/bin/bash

echo "=================================="
echo "NETWORK RECON TOOLKIT"
echo "=================================="

echo ""
echo "[+] Hostname"
hostname

echo ""
echo "[+] Current User"
whoami

echo ""
echo "[+] IP Address Information"
ip addr

echo ""
echo "[+] Routing Table"
ip route

echo ""
echo "[+] Active Network Connections"
netstat -an

echo ""
echo "Recon Complete"