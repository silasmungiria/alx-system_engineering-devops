# Web Infrastructure Design Project

## Overview

This project aims to design and implement a scalable, redundant, secured, and monitored web infrastructure for hosting the website www.foobar.com. The project will be completed in teams of three people, and it will be an ongoing second chance project that started on Jul 27, 2023, at 6:00 AM and must end by Aug 5, 2023, at 6:00 AM. The main goal is to understand and demonstrate proficiency in various web infrastructure concepts, such as DNS, monitoring, web servers, load balancers, databases, and more.

## Team Members

- Sylvain Kalache (Co-founder at Holberton School)
- Silas Mungiria (Team member)

## Learning Objectives

By the end of this project, the team is expected to achieve the following learning objectives:

- Design a web stack covering components from the SysAdmin/DevOps track projects.
- Explain the purpose and functionality of each component in the infrastructure.
- Implement system redundancy to minimize single points of failure.
- Familiarize with important acronyms like LAMP, SPOF, and QPS.

## Tasks

The project consists of several tasks, each building upon the previous ones. Here is an overview of the tasks:

1. Task 0: Simple Web Stack
   - Design a single-server web infrastructure for www.foobar.com.
   - Components: 1 server, 1 Nginx web server, 1 application server, 1 MySQL database.
   - Explain the role of each component and the domain name configuration.
   - Identify the DNS record type for the www subdomain.
   - Discuss the issues with this infrastructure, including SPOF, downtime during maintenance, and scalability limitations.

2. Task 1: Distributed Web Infrastructure
   - Design a three-server web infrastructure for www.foobar.com.
   - Components: 2 servers, 1 Nginx web server, 1 application server, 1 HAproxy load balancer, 1 MySQL database.
   - Justify the addition of each new element and explain the distribution algorithm used by the load balancer.
   - Differentiate between Active-Active and Active-Passive setups for the load balancer.
   - Describe how a Primary-Replica (Master-Slave) cluster works for the database and its implications on the application.
   - Analyze the issues with this infrastructure, including SPOF, security concerns, and lack of monitoring.

3. Task 2: Secured and Monitored Web Infrastructure
   - Design a three-server web infrastructure for www.foobar.com with security and monitoring in place.
   - Components: 3 firewalls, SSL certificate for HTTPS, 3 monitoring clients for Sumologic or other monitoring services.
   - Explain the purpose of adding firewalls, serving traffic over HTTPS, and implementing monitoring.
   - Describe the data collection process for the monitoring tool.
   - Provide guidelines on monitoring web server QPS.
   - Evaluate the issues with this infrastructure, including terminating SSL at the load balancer level, having a single MySQL server for writes, and identical server components.

4. Task 3: Scale Up (Advanced) - *Optional/Advanced*
   - Add components to scale up the infrastructure.
   - Components: 1 additional server, 1 HAproxy load balancer configured as a cluster, separate servers for web server, application server, and database.
   - Justify the addition of each new element for scalability.
   - Discuss the benefits of splitting components into individual servers.
   - Consider scalability and future expansion in the design.

## Project Requirements

- Each task should be whiteboarded, and a picture/screenshot of the diagram should be included in the project folder.
- The project will be manually reviewed, so ensure all tasks are completed and meet the learning objectives.
- Use English for all project-related documentation and explanations.
- Avoid plagiarism and provide original solutions for each task.
- Create a detailed README.md file at the root of the project folder.

## How to Submit

- Push your project files to the GitHub repository provided.
- Insert the GitHub file links into the URL box for each task.
- During whiteboarding sessions, no computers or notes will be allowed.

## Copyright and Plagiarism

- Plagiarism is strictly forbidden and will result in removal from the program.
- Do not publish any content from this project.

## Additional Notes

- Keep in mind the learning objectives and focus on meeting the requirements for each task without unnecessary verbosity.
- The project aims to test your understanding of web infrastructure design concepts, so be prepared to explain your solutions to mentors, staff, or students during the whiteboarding sessions.

### Happy coding!
