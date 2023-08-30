# 0x0C Web Server Project

This project focuses on configuring and managing a web server using Nginx. Throughout the project, you will set up a web server, configure domain names, implement redirects, and customize error pages. By completing the tasks, you'll gain a better understanding of web server concepts and automation techniques.

## Background Context

In this project, you'll work on configuring an Nginx web server while automating tasks using Bash scripts and Puppet manifests. The goal is to ensure your server is configured according to the specified requirements and to automate processes to improve efficiency.

## Concepts

For this project, it's important to understand the concept of [Child Process](#) in the context of server management.

## Resources

- [How the web works](#)
- [Nginx](#)
- [How to Configure Nginx](#)
- [Child process concept page](#)
- [Root and sub domain](#)
- [HTTP requests](#)
- [HTTP redirection](#)
- [Not found HTTP response code](#)
- [Logs files on Linux](#)
- [RFC 7231 (HTTP/1.1)](#)
- [RFC 7540 (HTTP/2)](#)
- `man scp`
- `man curl`

## Learning Objectives

By the end of this project, you will be able to explain the following concepts without external assistance:

- The main role of a web server
- The concept of a child process
- The reason web servers use parent and child processes
- The key HTTP requests
- What DNS stands for and its main role
- Various DNS record types (A, CNAME, TXT, MX)

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted on Ubuntu 16.04 LTS
- All files should end with a new line
- A `README.md` file, at the root of the project folder, is mandatory
- All Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7) without any errors
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining the script's purpose
- You can't use `systemctl` for restarting a process

## Tasks

1. [Transfer a file to your server](./0-transfer_file)
    - Write a Bash script that transfers a file from the client to a server using `scp`.

2. [Install nginx web server](./1-install_nginx_web_server)
    - Install Nginx on your `web-01` server and configure it to listen on port 80.

3. [Setup a domain name](./2-setup_a_domain_name)
    - Configure your DNS records with an A entry to point your root domain to your `web-01` IP address.

4. [Redirection](./3-redirection)
    - Configure your Nginx server to redirect `/redirect_me` to another page.

5. [Not found page 404](./4-not_found_page_404)
    - Configure your Nginx server to have a custom 404 page containing the string "Ceci n'est pas une page."

6. [Install Nginx web server (w/ Puppet)](./7-puppet_install_nginx_web_server.pp) - *Advanced*
    - Install and configure Nginx using a Puppet manifest, including a 301 redirect for `/redirect_me`.

## Author

Project by Sylvain Kalache and Silas Mugambi.
