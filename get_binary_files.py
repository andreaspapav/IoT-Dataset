import pyshark
packets = pyshark.FileCapture(
            input_file="capture1.pcap",
            use_json=True,
            include_raw=True
          )._packets_from_tshark_sync() # pcap_dir is the directory of my pcap file

hex_packet = packets.__next__().frame_raw.value
print(hex_packet)

binary_packet = bytearray.fromhex(hex_packet)
print(binary_packet)
f = open('packet1.bin', 'w+b')
f.write(binary_format)
f.close()