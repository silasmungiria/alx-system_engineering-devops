# 0x08. Networking Basics #1

This project is part of the DevOps curriculum and focuses on networking basics. The goal of this project is to further enhance your understanding of networking concepts and protocols. By the end of this project, you should be able to explain localhost, 0.0.0.0, the hosts file, and display active network interfaces on your machine.

## Resources

Read or watch the following materials to gain knowledge about the topics covered in this project:

- What is localhost
- What is 0.0.0.0
- What is the hosts file
- Netcat examples

Make use of the `man` command or other available resources to access the documentation for the following commands:

- `ifconfig`
- `telnet`
- `nc`
- `cut`

## Learning Objectives

By the end of this project, you should be able to:

- Understand the concept of localhost (127.0.0.1) and its purpose.
- Understand the purpose of 0.0.0.0 and how it relates to network interfaces.
- Understand the role of the hosts file (/etc/hosts) in DNS resolution.
- Display and identify the active network interfaces on your machine.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- A README.md file, at the root of the project folder, is mandatory
- All Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.7.0 via apt-get) without any errors
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script does

## Project Tasks

### 0. Change your home IP

Write a Bash script that configures an Ubuntu server to modify the IP addresses for localhost and facebook.com.

### 1. Show attached IPs

Write a Bash script that displays all active IPv4 IPs on the machine it's executed on.

### 2. Port listening on localhost (Advanced)

Write a Bash script that listens on port 98 on localhost.

## General Instructions

- Ensure your scripts are executable using the `chmod` command.
- Your Bash scripts should be checked using `shellcheck` to ensure they pass without any errors.
- Use the provided repository for submitting your answers.
- Avoid plagiarism. Do not copy and paste someone else's work.
- Do not publish the content of this project publicly.
