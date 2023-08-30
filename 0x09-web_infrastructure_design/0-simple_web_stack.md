# Simple Web Infrastructure Design

![Infrastructure Design](https://github.com/Mugambi12/alx-system_engineering-devops/raw/master/0x09-web_infrastructure_design/0-simple_web_stack.jpg)

In this document, we will design a simple web infrastructure consisting of a single server with a LAMP stack. The goal is to host a website accessible via www.foobar.com. Let's begin by discussing the user's journey to access the website.

## User Accesses the Website

1. A user, through their computer's browser, initiates a request to access the website hosted at www.foobar.com.
2. The browser sends an HTTP request over the internet to the domain name www.foobar.com.

## Infrastructure Design

We'll design a simple web infrastructure that fulfills the requirements using the following components:

- **1 Server:** Hosting all components of the infrastructure.
- **1 Web Server (Nginx):** Handling incoming HTTP requests and serving static content.
- **1 Application Server:** Processing dynamic content and executing server-side code.
- **1 Application Files (Code Base):** Containing the application's code.
- **1 Database (MySQL):** Storing structured data used by the application.
- **1 Domain Name foobar.com:** Configured with a www record pointing to the server's IP address 8.8.8.8.

## Component Roles

To better understand the design, let's explore the roles of each component:

- **Server:** A physical or virtual machine hosting the entire web infrastructure.
- **Domain Name:** A human-readable address (www.foobar.com) used to access the website instead of using IP addresses.
- **DNS Record (www):** A CNAME record mapping the subdomain "www" to the main domain "foobar.com."
- **Web Server (Nginx):** Handles incoming HTTP requests, serves static content, and forwards dynamic requests to the application server.
- **Application Server:** Processes dynamic content, executes server-side code, and interacts with the database.
- **Database (MySQL):** Stores structured data used by the application.

## Issues with the Infrastructure

While this simple web infrastructure serves as a starting point, it has certain limitations:

1. **Single Point of Failure (SPOF):** Since all components are hosted on a single server, if it fails, the entire website becomes inaccessible.
2. **Downtime During Maintenance:** Restarting the web server during maintenance can lead to temporary unavailability.
3. **Limited Scalability:** As incoming traffic increases, a single server might struggle to handle the load efficiently.

In summary, this simple web infrastructure design has advantages in terms of ease of setup but faces challenges related to reliability, scalability, and maintenance. More advanced configurations involving load balancing, redundancy, and distributed systems would be required to address these limitations.
