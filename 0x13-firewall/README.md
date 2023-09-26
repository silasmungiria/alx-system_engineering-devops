# Project: Firewall Configuration

## Background Context

In this project, we will be focusing on configuring firewalls on our servers to enhance security and control incoming traffic.

## Concepts

For this project, you are expected to be familiar with:

- Web stack debugging

## Project Requirements

### General

- **Allowed Editors**: vi, vim, emacs
- **Operating System**: Ubuntu 16.04 LTS
- All files must end with a new line
- A `README.md` file at the root of the project directory is mandatory
- All Bash script files must be executable
- Bash scripts must pass Shellcheck (version 0.3.7) without any error
- The first line of all Bash scripts should be `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining the purpose of the script

## Tasks

### Task 0: Block All Incoming Traffic

- Install and configure the `ufw` firewall on `web-01` to block all incoming traffic except for specific TCP ports (22, 80, and 443).
- Provide the `ufw` commands used for the configuration.

### Task 1: Port Forwarding (Advanced)

- Configure `web-01`'s firewall to redirect traffic from port 8080/TCP to port 80/TCP.
- Provide the ufw configuration file with the modification.

---
