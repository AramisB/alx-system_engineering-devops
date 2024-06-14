README: Understanding Firewalls
Firewalls are security systems that monitor and control incoming and outgoing network traffic based on a set of security rules. They act as a barrier between your trusted internal network and external networks (like the internet), helping prevent unauthorized access, attacks, and data breaches.

Types of Firewalls by Delivery Method:
Hardware Firewall: A dedicated appliance that sits between your network and the internet. Offers strong security but can be expensive.
Software Firewall: A program installed on your computer or server. More affordable but may be less powerful.
Cloud-Based Firewall (FWaaS): A cloud-delivered firewall service offering scalability and flexibility, but reliant on internet speed.
Types of Firewalls by Technology:
Packet-Filtering Firewall: Inspects individual data packets and allows/blocks them based on source, destination, and port information. (Basic)
Stateful Inspection Firewall: Tracks connections (sessions) and allows/blocks traffic based on the connection state. (More advanced than packet filtering)
Application-Level Gateway (Proxy Firewall): Acts as an intermediary between your device and the internet, inspecting traffic at the application level and filtering based on specific applications and protocols.
Next-Generation Firewall (NGFW): Combines traditional firewall features with intrusion detection/prevention, deep packet inspection, and application control. (Advanced)
The best firewall type depends on your needs and network environment. Consider security requirements, budget, and network complexity when choosing.

Network vs Host-Based Firewalls
Network Firewall:
Central security checkpoint for your entire network (often at the internet connection point).
Controls traffic flow based on predefined rules (IP addresses, ports, protocols).
Protects all devices on the network.
Examples: Built-in router firewalls, dedicated business firewalls.
Host-Based Firewall:
Software installed directly on individual devices (laptops, desktops, servers).
Provides granular control over applications and programs accessing the network/internet.
Offers additional security for individual devices.
Examples: Built-in firewalls in Windows and macOS.
For optimal security, use both network and host-based firewalls for a layered defense strategy.

ufw (Uncomplicated Firewall) - Common Commands
ufw is a command-line firewall configuration tool available on Ubuntu and Debian-based systems. Here are some common flags:

ufw enable: Activates the firewall.
ufw disable: Deactivates the firewall.
ufw allow <port>: Allows incoming traffic on a specific port (e.g., ufw allow 80 for web traffic).
ufw deny <port>: Blocks incoming traffic on a specific port.
ufw allow <application>: Allows incoming traffic for a specific application (e.g., ufw allow OpenSSH).
ufw deny <application>: Blocks incoming traffic for a specific application.
ufw status: Shows the current firewall status.