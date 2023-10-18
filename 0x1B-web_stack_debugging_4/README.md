Certainly, here's a README.md file for your project "0x1B. Web stack debugging #4":


# 0x1B. Web stack debugging #4

## Project Information

- **Project Name:** 0x1B. Web stack debugging #4
- **Domain:** DevOps
- **Skills:** SysAdmin, Scripting, Debugging
- **Author:** Sylvain Kalache, co-founder at Holberton School
- **Weight:** 1

**Project Schedule:**

- Start: October 16, 2023, 6:00 AM
- End: October 20, 2023, 6:00 AM
- Checker Release: October 19, 2023, 6:00 AM
- Auto Review Deadline: Project end

## Requirements

### General

- All your files will be interpreted on Ubuntu 14.04 LTS
- All your files should end with a new line
- A README.md file at the root of the project folder is mandatory
- Your Puppet manifests must pass puppet-lint version 2.1.1 without any errors
- Your Puppet manifests must run without error
- Your Puppet manifests' first line must be a comment explaining what the Puppet manifest is about
- Your Puppet manifests files must end with the extension .pp
- Files will be checked with Puppet v3.4

### Install puppet-lint

To install puppet-lint, use the following commands:

```bash
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```

## Tasks

### 0. Sky is the limit, let's bring that limit higher

**Mandatory**

In this web stack debugging task, we are testing how well our web server setup featuring Nginx is doing under pressure, and it turns out it's not doing well; we are getting a huge amount of failed requests.

For the benchmarking, we are using ApacheBench, which is a popular tool in the industry. It allows you to simulate HTTP requests to a web server. In this case, we will make 2000 requests to the server with 100 requests at a time. We can see that 943 requests failed. Let's fix our stack so that we get to 0, and remember that when something is going wrong, logs are your best friends!

```bash
$ ab -c 100 -n 2000 localhost/
```

After running the benchmark, you can see the results and the changes made to fix the issue.

### 1. User limit

**Advanced**

Change the OS configuration so that it is possible to log in with the holberton user and open a file without any error message. This task involves resolving issues related to file limits.

```bash
$ su - holberton
```

After running the Puppet manifest for this task, you should be able to log in as the holberton user without encountering any errors.

## Repository Information

- **GitHub Repository:** [alx-system_engineering-devops](https://github.com/mugambi12/alx-system_engineering-devops)
- **Directory:** 0x1B-web_stack_debugging_4
- **Files:**
  - 0-the_sky_is_the_limit_not.pp
  - 1-user_limit.pp
---
