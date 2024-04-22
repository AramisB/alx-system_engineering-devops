Web Server and Network Essentials
This README provides a basic understanding of web servers, processes, and essential network protocols.

Web Server
Main Role: A web server is software that stores, processes, and delivers web content (web pages, images, etc.) to users when requested through a web browser. It acts as an intermediary between your device and the website you're trying to access.

Processes
Child Process: A child process is a new process created by an existing process (parent process). In web servers, the parent process manages worker processes (child processes) that handle incoming requests from users.

Parent and Child Processes in Web Servers
Web servers typically use a parent-child process model for efficiency. The parent process oversees the overall server operation and spawns child processes to handle individual client requests.
This approach allows the server to handle multiple requests concurrently without overloading the system.

Main HTTP Requests
GET: Retrieves information from a server (e.g., loading a web page).
POST: Submits data to a server (e.g., sending a form).
PUT: Uploads or updates data on a server.
DELETE: Removes data from a server.

DNS
What it Stands For: Domain Name System
Main Role: DNS translates human-readable domain names into machine-readable IP addresses (e.g., 142.250.184.196) that computers use to locate resources on the internet.  It acts like a phonebook for the internet.

DNS Record Types
A Record: Maps a domain name to an IP address (the most common record type).
CNAME Record: Points a domain name (alias) to another domain name (canonical name).
TXT Record: Stores arbitrary text data associated with a domain name (often used for verification or domain ownership claims).
MX Record: Specifies mail server(s) responsible for receiving email for a domain name.

scp
scp stands for Secure Copy. It's a command-line tool used for securely transferring files between computers on a network.
curl
curl is a command-line tool for transferring data from or to a server, often used for retrieving content from web servers for testing purposes.