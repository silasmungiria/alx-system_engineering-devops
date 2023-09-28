# Project Readme: 0x12. Web Stack Debugging #2

## Description

This project focuses on debugging web stack issues, specifically related to running Nginx as the `nginx` user instead of the default `root` user. Additionally, a script is created to allow execution of commands as another specified user.

## Tasks

### Task 0: Run software as another user

- **File:** `0-iamsomeoneelse`
- **Description:** This Bash script accepts one argument, which is a username. It runs the `whoami` command under the specified user.

### Task 1: Run Nginx as Nginx

- **File:** `1-run_nginx_as_nginx`
- **Description:** This Bash script configures the container to have Nginx running as the `nginx` user, listening on all active IPs on port 8080.

### Task 2: 7 lines or less (Advanced)

- **File:** `100-fix_in_7_lines_or_less`
- **Description:** Building on Task 1, this Bash script must be 7 lines or less, ensuring it remains concise while maintaining the necessary functionality.

## Environment

All files in this project are intended to be interpreted on Ubuntu 20.04 LTS. They end with a new line and are executable. They also pass Shellcheck without any errors.

## Usage

1. Clone the repository from GitHub: [alx-system_engineering-devops](https://github.com/username/alx-system_engineering-devops)
2. Navigate to the directory: `0x12-web_stack_debugging_2`
3. Execute the desired Bash script as needed for the task.

## Example

```bash
$ ./0-iamsomeoneelse www-data
www-data
```

```bash
$ ./1-run_nginx_as_nginx
# Output confirming successful configuration of Nginx
```

```bash
$ ./100-fix_in_7_lines_or_less
# Output confirming successful configuration of Nginx in 7 lines or less
```

## Author

Silas - [GitHub Profile](https://github.com/username)

---
