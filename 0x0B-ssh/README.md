Secure Shell (SSH) Access with Key-Based Authentication
This document provides an overview of SSH, key-based authentication, and related commands.

What is SSH?
SSH (Secure Shell) is a network protocol enabling secure remote access to a server. It encrypts user authentication (login) and data transfer, protecting your communication from eavesdropping and unauthorized access.

Benefits of SSH Key-Based Authentication:
Enhanced Security: Keys offer a more secure alternative to password-based authentication, which is susceptible to brute-force attacks.

Convenience: Once your public key is added to the server, you can connect without repeatedly entering your password.

Generating SSH Key Pair:
Open a terminal window on your local machine.
Run the following command, replacing your_email@example.com with your actual email address:

Bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

This command generates an RSA key pair (public and private).
The key size is set to 4096 bits for strong security.
You'll be prompted to enter a secure passphrase for your private key. Choose a strong passphrase and keep it confidential.

Adding Public Key to Server:
Copy the contents of the public key file (id_rsa.pub) on your local machine.
Paste the copied key into the authorized_keys file on the server you want to connect to. (Consult your server administrator for instructions on adding the key.)

Connecting with SSH Key Pair:
Open a terminal window on your local machine.
Run the following command, replacing user with your username and server_address with the server's IP address or hostname:
Bash
ssh user@server_address

You might be prompted to confirm the server's fingerprint for the first connection. Verify it matches the expected fingerprint (obtain from the server administrator if unsure).

If it's the first time connecting with this key pair, you'll be prompted for the passphrase you created earlier.

Using #!/usr/bin/env bash
When writing shell scripts, consider using #!/usr/bin/env bash instead of /bin/bash at the beginning of the script. This ensures portability by searching for the Bash interpreter in the system's PATH environment variable, regardless of its specific location.
