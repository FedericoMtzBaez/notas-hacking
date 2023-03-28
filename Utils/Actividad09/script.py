from  scapy.all import *

packets = rdpcap('capture.pcap')

for p in packets:
	if UDP in p  and p[UDP].dport==22:
		if p[UDP.sport > 5000:
			flag += chr(p[UDP].sport - 5000)
print(flag)
