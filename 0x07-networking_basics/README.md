Networking Basics: A Primer
This document provides a basic introduction to key networking concepts.

The OSI Model
The Open Systems Interconnection (OSI) model is a conceptual framework that defines seven layers for network communication. Each layer has specific responsibilities, enabling various network devices and software to interact seamlessly. Understanding the OSI model helps visualize and troubleshoot networking issues.

Types of Networks
Networks can be categorized based on their size and scope:

LAN (Local Area Network): A network connecting devices within a limited physical area, like a home, office, or school.
WAN (Wide Area Network): A network spanning a larger geographical area, connecting geographically dispersed LANs, often using leased lines or public networks.
Internet: A global system of interconnected networks that allows communication between computers across the world.
Network Addressing
MAC Address: A unique identifier (hardware address) assigned to a network interface controller (NIC) of a device. Used for communication on the local network (Layer 2 - Data Link Layer).
IP Address: A unique logical address assigned to a device on an IP network (Layer 3 - Network Layer). It helps route data packets across the network to their intended destination.
Types of IP Addresses:

Private Addresses: Not routable on the public internet, used for internal communication within a private network.
Public Addresses: Unique addresses assigned to devices on the public internet, enabling communication between devices across different networks.
IP Version:

IPv4: The most widely used version, but facing depletion due to its limited address space.
IPv6: The next generation of IP addressing with a significantly larger address space, gradually being adopted.
Localhost
Refers to the loopback interface (address 127.0.0.1) of a device, used for testing and communication within the same device.

Transport Protocols
TCP (Transmission Control Protocol): Provides reliable, ordered delivery of data with error checking and retransmission mechanisms. Used for applications requiring high accuracy, like file transfers.
UDP (User Datagram Protocol): Offers faster but connectionless communication without error checking or guaranteed order. Used for applications prioritizing speed over reliability, like streaming media.
TCP/UDP Ports:

Each service or application uses specific ports (numbered channels) to communicate on the network. Common port numbers are documented for various services.

Network Diagnostics
ping: A tool used to check network connectivity by sending and receiving data packets to a specific host. It measures the round-trip time (RTT) for packets and helps identify network reachability issues.
Additional Resources:

man or help: Command-line tools for accessing manual pages on specific commands.
netstat: A network monitoring tool that displays information about network connections, routing tables, and other network-related statistics.
