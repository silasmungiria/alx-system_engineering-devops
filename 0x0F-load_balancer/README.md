# 0x0F Load Balancer

## Table of Contents
- [Project Description](#project-description)
- [Concepts](#concepts)
- [Background Context](#background-context)
- [Resources](#resources)
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [1. Double the Number of Webservers](#1-double-the-number-of-webservers)
  - [2. Install Your Load Balancer](#2-install-your-load-balancer)
  - [3. Add a Custom HTTP Header with Puppet (Advanced)](#3-add-a-custom-http-header-with-puppet-advanced)

---

## Project Description

This project aims to improve our web stack by introducing redundancy for our web servers, allowing us to handle more traffic and enhance infrastructure reliability. We'll achieve this by configuring two additional servers: `web-02` and `lb-01`.

## Concepts

For this project, you should be familiar with the following concepts:
- Load balancer
- Web stack debugging

## Background Context

You've been provided with two additional servers: `gc-[STUDENT_ID]-web-02-XXXXXXXXXX` and `gc-[STUDENT_ID]-lb-01-XXXXXXXXXX`. The goal is to configure these servers to achieve redundancy for our web servers and improve infrastructure reliability.

## Resources

Before you start, it's recommended to read or watch the following resources:
- [Introduction to load-balancing and HAproxy](https://intranet.alxswe.com/rltoken/B7f3oz8i3Xvvom_YQZzLnQ)
- [HTTP header](https://intranet.alxswe.com/rltoken/sZ9v3Vq2tgLwN_PWVQketw)
- [Debian/Ubuntu HAProxy packages](https://intranet.alxswe.com/rltoken/2VRAgtKKR9g6Xfb0xzGiSg)

## Requirements

### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script is doing

### Your Servers
- Name, Username, IP, and State:
  - 91903-web-01, ubuntu, 54.197.105.254, running
  - 91903-web-02
  - 91903-lb-01

## Tasks

### 1. Double the Number of Webservers

**Mandatory** | Score: 0.0%
Configure `web-02` to be identical to `web-01`. Automate this process by writing a Bash script. Additionally, configure Nginx on both `web-01` and `web-02` to include a custom HTTP response header, `X-Served-By`, with the server's hostname.

#### Requirements:
- Configure Nginx on `web-01` and `web-02` to include a custom HTTP header
- Custom HTTP header name: X-Served-By
- Custom HTTP header value: The hostname of the server Nginx is running on
- Write `0-custom_http_response_header` script to configure a new Ubuntu machine to meet these requirements
- Ignore SC2154 for shellcheck

Example:
```bash
sylvain@ubuntu$ curl -sI 34.198.248.145 | grep X-Served-By
X-Served-By: 03-web-01
sylvain@ubuntu$ curl -sI 54.89.38.100 | grep X-Served-By
X-Served-By: 03-web-02
sylvain@ubuntu$
```

### 2. Install Your Load Balancer

**Mandatory** | Score: 0.0%
Install and configure HAproxy on `lb-01` server. Configure HAproxy to distribute traffic evenly between `web-01` and `web-02` using a round-robin algorithm. Ensure HAproxy can be managed via an init script.

#### Requirements:
- Configure HAproxy to distribute traffic to `web-01` and `web-02`
- Use a round-robin algorithm for load balancing
- Ensure HAproxy can be managed via an init script
- Ensure your servers are configured with the right hostnames: `[STUDENT_ID]-web-01` and `[STUDENT_ID]-web-02`

Example:
```bash
sylvain@ubuntu$ curl -Is 54.210.47.110
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Mon, 27 Feb 2017 06:12:17 GMT
Content-Type: text/html
...
X-Served-By: 03-web-01
Accept-Ranges: bytes
```

### 3. Add a Custom HTTP Header with Puppet (Advanced)

**Advanced** | Score: 0.0%
Automate the task of creating a custom HTTP header response, similar to task #1, but with Puppet.

#### Requirements:
- Name of the custom HTTP header: X-Served-By
- Value of the custom HTTP header: The hostname of the server Nginx is running on
- Write `2-puppet_custom_http_response_header.pp` script to configure a new Ubuntu machine to meet these requirements
