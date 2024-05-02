What is HTTPS?
HTTPS (Hypertext Transfer Protocol Secure) is a secure version of HTTP, the protocol over which data is sent between your browser and the website you are connected to. It adds a layer of encryption to protect the data during transmission.

Main Elements of SSL
SSL (Secure Sockets Layer) provides two main elements:
Encryption: SSL encrypts the data transmitted between the client and the server, ensuring that it cannot be intercepted and read by unauthorized parties.
Authentication: SSL verifies the identity of the server, ensuring that the client is connecting to the intended website and not an imposter.

HAProxy SSL Termination
HAProxy SSL termination refers to the practice of decrypting SSL-encrypted traffic at the load balancer (HAProxy), allowing it to inspect and possibly modify the traffic before forwarding it to the backend servers. The purpose of encrypting traffic is to enhance security and protect sensitive information, such as usernames, passwords, and financial data, from being intercepted and accessed by malicious actors.

Bash Functions
awk
awk is a powerful programming language primarily used for text processing and data extraction. It operates on records (lines) and fields (columns) within structured data files. Some common flags include:

-F: Specify a field separator.
-v: Assign a variable.
NR: Number of the current record.
NF: Number of fields in the current record.
BEGIN and END: Special patterns to execute actions before processing and after processing, respectively.

dig
dig (Domain Information Groper) is a command-line tool used for querying DNS (Domain Name System) servers. It provides detailed information about DNS records associated with domain names, such as IP addresses, name servers, and other DNS-related data. Some common flags include:

+short: Display only the short form of the output.
+trace: Perform a trace of DNS delegation for the specified domain.
+noall: Disable all default output options.
+answer: Display only the answer section of the DNS response.
