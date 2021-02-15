import pyshark
packets = pyshark.FileCapture(
            input_file="capture1.pcap",
            use_json=True,
            include_raw=True
          )

counter = 1
length = len(packets)
print(length)
for packet in packets:
	hex_packet = packet.frame_raw.value
	print(hex_packet)
	binary_packet = bytearray.fromhex(hex_packet)
	#print(binary_packet)
	name = "binary_files/" + str(counter) + ".bin"
	f = open(name, 'w+b')
	f.write(binary_packet)
	f.close()
	counter += 1
