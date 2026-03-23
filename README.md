# CS333-network-utils-sudo-rm-rf-The_Team

This repository contains a collection of network utilities designed to dissessemble and ressemble IP packets. 

# TEAM NAMES
- Sam Wilcox
- Danner Hill
- Tanner Klinge

# Steps
- Install UV
- Network structure packet

## Network Packet Structure
## IP Packet
-  Version (4 bits): Indicates the IP version (IPv4 or IPv6).
- Header Length (4 bits): Specifies the size of the IP header, helping the receiver separate header from data.
- Type of Service (8 bits): Marks the packet for prioritization and quality of service (QoS).
- Total Length (16 bits): Total size of the IP packet, including header and data.
- Identification (16 bits): Unique ID used when packets are fragmented for reassembly.
- Flags (3 bits): Control fragmentation, such as “Don’t Fragment” or “More Fragments” indicators.
- Fragment Offset (13 bits): Indicates the position of this fragment in the original packet.
- Time to Live (TTL) (8 bits): Limits the number of hops a packet can travel to prevent infinite circulation.
- Protocol (8 bits): Specifies the transport protocol (e.g., TCP = 6, UDP = 17) carried in the data field.
- Header Checksum (16 bits): Detects errors in the IP header for integrity verification.
- Source IP Address (32 bits): Logical address of the sender device.
- Destination IP Address (32 bits): Logical address of the receiver device.
- Options (Variable length): Optional features like security, routing, and timestamps.
- Data/Payload: Encapsulates the TCP segment or other transport-layer data.

## TCP Packet
- Source Port: This port identifies the port number of the application that sends the data.
- Destination Port: Identify the port number of the application that should receive the data.
- Sequence Number: Specifies the position of the first byte of data in this segment, ensuring that data can be reassembled in the correct order at the receiver.
- Acknowledgment Number: Confirms the successful receipt of data and indicates the next byte the sender should transmit.
- Data Offset (Header Length): Indicates where the actual data begins in the packet, allowing the receiver to separate headers from user data.
- Control Flags: Include bits like SYN, ACK, FIN, RST that control connection setup, maintenance, and termination.
- Window Size: Determines the amount of data the receiver can accept at a time, providing flow control to prevent overwhelming the receiver.
- Checksum: Used to detect errors in the header and data, ensuring integrity during transmission.
- Urgent Pointer: Points to urgent data that should be processed immediately, if any.
- Options: Provides additional features such as maximum segment size (MSS) or timestamps to improve performance.
- Data (Payload): The actual application data being sent, like a message, file, or web content.

## Sources
- https://www.geeksforgeeks.org/computer-networks/tcp-ip-packet-format/
- https://inc0x0.com/tcp-ip-packets-introduction/tcp-ip-packets-3-manually-create-and-send-raw-tcp-ip-packets/