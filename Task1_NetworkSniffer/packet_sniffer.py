from scapy.all import sniff, IP, TCP, UDP, ICMP

def analyze_packet(packet):
    print("="*60)
    if IP in packet:
        ip_layer = packet[IP]
        print(f"📦 IP Packet:")
        print(f"🔹 Source IP: {ip_layer.src}")
        print(f"🔹 Destination IP: {ip_layer.dst}")
        print(f"🔹 Protocol: {ip_layer.proto}")

        if TCP in packet:
            tcp_layer = packet[TCP]
            print(f"🔸 Protocol: TCP")
            print(f"   - Source Port: {tcp_layer.sport}")
            print(f"   - Destination Port: {tcp_layer.dport}")
        elif UDP in packet:
            udp_layer = packet[UDP]
            print(f"🔸 Protocol: UDP")
            print(f"   - Source Port: {udp_layer.sport}")
            print(f"   - Destination Port: {udp_layer.dport}")
        elif ICMP in packet:
            print(f"🔸 Protocol: ICMP")

        payload = bytes(packet[IP].payload)
        if payload:
            print(f"📄 Payload (first 100 bytes):\n{payload[:100]}")
    else:
        print("Non-IP Packet Detected")

print("✅ Code reached sniff() function, now waiting for packets...")
sniff(prn=analyze_packet, count=10)
