FILE_NAME="test.bin"

# import csv
# import struct

#  with open('FILE_NAME') as logfile:
#    for row in csv.reader(logfile):
#     = row
#    ints = [10,50,100,2500,256]
#    with open('output', 'w') as fh:
#    data = struct.pack('i' * len(ints), *ints)
#    fh.write(data)



def to_bin(var):
    print("Write var to disk in binary format")
    packet1 = Packet("192.168.1.1")
    packet1.to_binary()

def from_bin():
    print("Reading binary file to mem")

if __name__ == "__main__":
    print("In the main file")
    to_bin(10)
    var = from_bin()
    print(var)

class Packet:
    def __init__(self, source_ip, dest_ip, payload):
        self.source_ip = source_ip
        self.dest_ip = dest_ip
        self.payload = payload

    def to_binary(self):
        with open('output.bin', 'wb') as f:
            for p in self.source_ip.split('.'):
                f.write(int(p).to_bytes(1, btyeorder='big'))
        print("Packet written to output.bin in binary format.")

        def __str__(self):
            return f"Packet from {self.source_ip} to {self.dest_ip} with payload: {self.payload}"