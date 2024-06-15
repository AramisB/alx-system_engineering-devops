Application Servers vs Web Servers and Deploying Flask Apps on Ubuntu 16.04

This document covers two main topics:

1. Understanding Application Servers vs Web Servers

What is a Web Server?

A web server acts as the gatekeeper for your website. It delivers static content like HTML pages, images, and videos to users' web browsers. It communicates using Hypertext Transfer Protocol (HTTP) and might support additional protocols like FTP and SMTP. Popular web servers include Apache and Nginx.

What is an Application Server?

An application server sits behind the web server and handles complex tasks. It processes user interactions, connects to databases, and generates dynamic content. It executes server-side code and supports various protocols beyond HTTP. Application servers often use features like multithreading for high concurrency. Examples include JBoss and Tomcat.

Analogy: Imagine a restaurant. The web server is the waiter, delivering your pre-made menu (static content) to your table. The application server is the kitchen, processing your order (user interaction), retrieving ingredients from the pantry (database), and preparing your custom dish (dynamic content).

2. Deploying a Flask Application with Gunicorn and Nginx on Ubuntu 16.04

This guide outlines how to serve your Flask application using Gunicorn and Nginx on Ubuntu 16.04.

Prerequisites:

Update system packages:
sudo apt update && sudo apt upgrade

Install dependencies:
sudo apt install python-pip python-dev libpq-dev nginx

Develop Your Flask Application:
Create your project directory and Flask application code.
Ensure your Flask app runs with flask run.
Configure Gunicorn (without virtualenv):

WSGI Entry Point: Create wsgi.py in your project directory:

Python
from your_flask_app import app  # Replace with your app's name

if __name__ == "__main__":
    from gunicorn.main import run

    run(app, workers=2)  # Adjust workers as needed

Systemd Unit File (Optional): Create myproject.service (replace with your project name) in /etc/systemd/system/:

[Unit]
Description=My Flask Application
After=network.target

[Service]
User=your_user  # Replace with the user running the application
Group=www-data
WorkingDirectory=/path/to/your/project  # Replace with your project directory
ExecStart=/usr/bin/gunicorn --bind 127.0.0.1:8000 wsgi:app

[Install]
WantedBy=multi-user.target

Replace placeholders and run:

sudo systemctl daemon-reload
sudo systemctl enable myproject.service

Configure Nginx as a Reverse Proxy:
Nginx Configuration: Create a server block configuration file for your application (usually in /etc/nginx/sites-available/). Name it according to your domain or subdomain (e.g., your_app.conf):

server {
    listen 80;  # Adjust port if needed
    server_name your_domain_or_ip;  # Replace with your domain or IP

    location / {
        proxy_pass http://127.0.0.1:8000;  # Adjust IP and port based on Gunicorn configuration
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_redirect off;
    }
}
Enable Nginx Configuration:

Activate the configuration file:
sudo ln -s /etc/nginx/sites-available/your_app.conf /etc/nginx/sites-enabled/

Test configuration:
sudo nginx -t

Reload Nginx:
sudo systemctl reload nginx

Test and Access Your Application:

Start your Gunicorn service if using a systemd unit file:
sudo systemctl start myproject.service

Access your application through the configured domain name or IP address in your web browser.
Additional Notes:
Replace placeholders with your specific configurations.
Implement HTTPS for production environments.
Refer to Gunicorn: https://docs.gunicorn.