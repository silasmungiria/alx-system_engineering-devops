# 0x1A Application Server

## Table of Contents
* [Project Description](#project-description)
* [Concepts](#concepts)
* [Requirements](#requirements)
* [Tasks](#tasks)
  * [Set up development with Python](#set-up-development-with-python)
  * [Set up production with Gunicorn](#set-up-production-with-gunicorn)
  * [Serve a page with Nginx](#serve-a-page-with-nginx)
  * [Add a route with query parameters](#add-a-route-with-query-parameters)
  * [Serve your AirBnB clone](#serve-your-airbnb-clone)
  * [Deploy it!](#deploy-it)
  * [No service interruption (Advanced)](#no-service-interruption-advanced)

## Project Description

In this project, you will enhance your web infrastructure by setting up an application server, serving dynamic content, and handling different routing scenarios using Nginx. The goal is to serve your Airbnb clone project and ensure smooth functionality.

## Concepts

In this project, you will work with the following concepts:
- Web Server
- Server
- Web stack debugging

## Requirements

- A README.md file at the root of the project folder is mandatory.
- Everything Python-related must be done using python3.
- All configuration files must have comments.
- All your files will be interpreted on Ubuntu 16.04 LTS.
- All your files should end with a new line.
- All your Bash script files must be executable.
- Your Bash scripts must pass Shellcheck without any errors.
- The first line of all your Bash scripts should be `#!/usr/bin/env bash`.
- The second line of all your Bash scripts should be a comment explaining what the script does.

## Tasks

### Set up development with Python

#### Requirements:
- Make sure that task #3 of your SSH project is completed for web-01. The checker will connect to your servers.
- Install the net-tools package on your server: `sudo apt install -y net-tools`
- Git clone your AirBnB_clone_v2 on your web-01 server.
- Configure the file `web_flask/0-hello_route.py` to serve its content from the route `/airbnb-onepage/` on port 5000.
- Your Flask application object must be named `app`.

### Set up production with Gunicorn

#### Requirements:
- Install Gunicorn and any other libraries required by your application.
- The Flask application object should be called `app`.
- Serve the content from the same route as in the previous task.
- The Gunicorn instance should listen on port 5000.

### Serve a page with Nginx

#### Requirements:
- Configure Nginx to serve your page from the route `/airbnb-onepage/`.
- Nginx must serve this page both locally and on its public IP on port 80.
- Nginx should proxy requests to the process listening on port 5000.

### Add a route with query parameters

#### Requirements:
- Configure Nginx to proxy requests to the route `/airbnb-dynamic/number_odd_or_even/(any integer)` to a Gunicorn instance listening on port 5001.
- Nginx must serve this page both locally and on its public IP on port 80.

### Serve your AirBnB clone

#### Requirements:
- Git clone your AirBnB_clone_v4.
- Your Gunicorn instance should serve content from `web_dynamic/2-hbnb.py` on port 5003.
- Setup Nginx to serve the static assets found in `web_dynamic/static/`.
- Update `web_dynamic/static/scripts/2-hbnb.js` to the correct IP.

### Deploy it! (Advanced)

#### Requirements:
- Write a systemd script to start a Gunicorn process serving content from `web_dynamic/2-hbnb.py`.
- The Gunicorn process should have 3 worker processes.
- The process should log errors in `/tmp/airbnb-error.log`.
- The process should log access in `/tmp/airbnb-access.log`.
- The process should be bound to port 5003.

### No service interruption (Advanced)

#### Requirements:
- Write a Bash script to reload Gunicorn gracefully.
- The script should gracefully shut down and renew workers to update the application without downtime.

*This project must be completed within the specified time frame.*

## Author
- Sylvain Kalache, co-founder at Holberton School
- Silas Mugambi, student at ALX Africa School

## Project Timeline
- Project started on Oct 16, 2023, at 6:00 AM and must end by Oct 20, 2023, at 6:00 AM.
- Checker was released on Oct 18, 2023, at 8:24 PM.
- An auto review will be launched at the deadline.

## Servers
| Name          | Username | IP             | State   |
|---------------|----------|-----------------|---------|
| 91903-web-01  | ubuntu   | 54.197.105.254  | running |
| 91903-web-02  | ubuntu   | 100.24.206.145 | running |
| 91903-lb-01   | ubuntu   | 54.224.25.16   | running |

---
