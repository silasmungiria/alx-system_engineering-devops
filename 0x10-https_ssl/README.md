# Project: HTTPS SSL Configuration

## Background Context

In this project, we will be configuring our servers to ensure secure website traffic using HTTPS SSL. This involves setting up SSL termination on HAProxy, redirecting HTTP traffic to HTTPS, and making sure that our domain is correctly configured.

## Learning Objectives

Upon completion of this project, you should be able to explain the following concepts without the need for external resources:

- What HTTPS SSL serves as in a web environment.
- The purpose of encrypting traffic.
- What SSL termination means.

## Project Requirements

### General

- **Allowed Editors**: vi, vim, emacs.
- **Operating System**: Ubuntu 16.04 LTS.
- All files must end with a new line.
- A `README.md` file at the root of the project directory is mandatory.
- All Bash script files must be executable.
- Bash scripts must pass Shellcheck (version 0.3.7) without any error.
- The first line of all Bash scripts should be `#!/usr/bin/env bash`.
- The second line of all Bash scripts should be a comment explaining the purpose of the script.

## Tasks

### Task 0: World Wide Web

**Objective**: Configure your domain zone to point to the load balancer IP and create a Bash script to display information about subdomains.

- Add the subdomain `www` to your domain, pointing it to the load balancer IP (`lb-01`).
- Add the subdomains `lb-01`, `web-01`, and `web-02` to your domain, pointing them to their respective IPs.
- Create a Bash script that accepts two arguments: `domain` and `subdomain`.
- Output information about the specified subdomain.

### Task 1: HAProxy SSL Termination

**Objective**: Configure HAProxy to handle encrypted traffic and serve it to the web servers.

- HAProxy should listen on port TCP 443.
- HAProxy should accept SSL traffic.
- HAProxy should serve encrypted traffic that returns the root page of the web server.
- The page returned should contain the text "Holberton School".
- Provide your HAProxy configuration file as `1-haproxy_ssl_termination`.

### Task 2: No Loophole in Your Website Traffic

**Objective**: Enforce HTTPS traffic by redirecting HTTP requests to HTTPS.

- Configure HAProxy to automatically redirect HTTP traffic to HTTPS.
- The redirection should be transparent to the user and return a 301 status code.
- Provide your HAProxy configuration file as `100-redirect_http_to_https`.

---
