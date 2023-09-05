# 0x0F. Load Balancer Project

**Author:** Sylvain Kalache, co-founder at Holberton School
**Weight:** 1
**Project Start:** Sep 4, 2023 6:00 AM
**Project End:** Sep 5, 2023 6:00 AM
**Checker Release:** Sep 4, 2023 12:00 PM

## Table of Contents

- [Project Description](#project-description)
- [Concepts](#concepts)
- [Background Context](#background-context)
- [Resources](#resources)
- [Requirements](#requirements)
- [Tasks](#tasks)
  1. [Double the number of webservers](#task-0-double-the-number-of-webservers)
  2. [Install your load balancer](#task-1-install-your-load-balancer)
  3. [Add a custom HTTP header with Puppet](#task-2-add-a-custom-http-header-with-puppet)

---

## Project Description

The 0x0F Load Balancer project aims to enhance the web stack by introducing redundancy for web servers. This redundancy will allow the infrastructure to handle more traffic by doubling the number of web servers, ensuring high availability. The key component in achieving this is the use of a load balancer.

In this project, you will write Bash scripts to automate the configuration of a brand new Ubuntu server to meet the project requirements. Additionally, you will configure Nginx to include a custom HTTP response header to track the web server handling HTTP requests. The project will also involve the installation and configuration of HAProxy as the load balancer.

---

## Concepts

This project is centered around the following concepts:

- Load balancer
- Web stack debugging

---

## Background Context

You have been provided with two additional servers:

- `gc-[STUDENT_ID]-web-02-XXXXXXXXXX`
- `gc-[STUDENT_ID]-lb-01-XXXXXXXXXX`

The primary objective is to configure these servers to create redundancy for web servers. This redundancy will ensure that even if one web server fails, the other will continue to handle requests.

To achieve this, you need to write Bash scripts that automate the configuration of the servers. All scripts should be designed to set up a new Ubuntu server according to the task requirements.

---

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script is doing

### Your Servers

| Name             | Username | IP           | State              |
|------------------|----------|--------------|--------------------|
| 91903-web-01     |          |              |                    |
| 91903-web-02     |          |              |                    |
| 91903-lb-01      |          |              |                    |

---

## Tasks

- Task 0: Double the number of webservers
- Task 1: Install your load balancer
- Task 2: Add a custom HTTP header with Puppet
