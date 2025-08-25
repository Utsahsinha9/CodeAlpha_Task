# Task 1: Network Packet Sniffer

This task is part of the CodeAlpha Cybersecurity Virtual Internship.

## 📚 Objective

Build a Python-based network packet sniffer that can capture and analyze packets in real-time to understand the structure of network data and protocols.

---

## 📂 Deliverables

- 🐍 `packet_sniffer.py` — Python script using Scapy for packet capture and analysis
- 📄 Optional: `sample_output.txt` — Contains example output from sniffed packets

---

## 🔍 Features

- Captures real-time network traffic
- Displays:
  - Source & Destination IPs
  - Protocol type (TCP, UDP, ICMP)
  - Port numbers
  - First 100 bytes of packet payload
- Uses Scapy library for low-level packet access

---

## ▶️ How to Run

1. Install required library:

pip install scapy

bash
Copy
Edit

2. Run the script with admin/root privileges: