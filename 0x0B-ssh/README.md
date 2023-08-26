# 0x0B SSH Project

This project focuses on SSH (Secure Shell), covering various aspects such as key pairs, configuration files, and secure connections. By the end of this project, you will have a better understanding of SSH concepts and be able to use SSH for secure remote access.

## Background Context

This project involves connecting to an Ubuntu server using SSH and an RSA key pair. The server's information is available in the my servers section of the intranet. The tasks will require you to perform various SSH-related activities using Bash scripts, configuration files, and Puppet.

## Resources

### Read or watch:
- [What is a (physical) server - text](#https://intranet.alxswe.com/rltoken/dkgW9lKiBRiUZHfq0MDJuw)
- [What is a (physical) server - video](#https://intranet.alxswe.com/rltoken/AxFcTdcXUCsrVp01X_EbFA)
- [SSH essentials](#https://intranet.alxswe.com/rltoken/ux0eM1QU9reNyG45b0erAQ)
- [SSH Config File](#https://intranet.alxswe.com/rltoken/Rc9FpSy4ZaQWPlcWLinbNw)
- [Public Key Authentication for SSH](#https://intranet.alxswe.com/rltoken/tOcxk5mtkedBM0WxyDZxTw)
- [How Secure Shell Works](#https://intranet.alxswe.com/rltoken/j0atjRrVfZ6F810qmPfAzA)
- [SSH Crash Course](#https://intranet.alxswe.com/rltoken/FKqd8CjxExmpWGu6xGavKw)

### For reference:

- [Understanding the SSH Encryption and Connection Process](#https://intranet.alxswe.com/rltoken/JB-Vi4dR3q6nF4MBhsn8kQ)
- [Secure Shell Wiki](#https://intranet.alxswe.com/rltoken/SpiYWE79Yfr_vWDg42dzCw)
- [IETF RFC 4251](#https://intranet.alxswe.com/rltoken/f2O0OQq9tch2MYeNAzkg5w)
- [Internet Engineering Task Force](#https://intranet.alxswe.com/rltoken/gd1W1UvB0KeJVWwM8BLvhA)
- [Request for Comments](#https://intranet.alxswe.com/rltoken/jb-IrnQnUh-PsEDlbAU0Kw)

### man or help:
- `man ssh`
- `man ssh-keygen`
- `man env`

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- A `README.md` file at the root of the project folder is mandatory
- All Bash script files must be executable
- The first line of all Bash scripts should be `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining the script's purpose
- Your SSH client configuration file must be updated for specific requirements

## Tasks

1. [Use a private key](./0-use_a_private_key)
    - Write a Bash script that connects to your server using the private key `~/.ssh/school` and the user `ubuntu`.

2. [Create an SSH key pair](./1-create_ssh_key_pair)
    - Write a Bash script that creates an RSA key pair with specific attributes.

3. [Client configuration file](./2-ssh_config)
    - Update your SSH client configuration file to use the private key `~/.ssh/school` and refuse password authentication.

4. [Let me in!](./3-ssh_key_upload)
    - Add an SSH public key to your server's authorized keys so that others can connect using the `ubuntu` user.

5. [Client configuration file (w/ Puppet)](./0x0B-ssh/100-puppet_ssh_config.pp)
    - Use Puppet to update your SSH client configuration file for passwordless and secure authentication.

## Author

Project by Sylvain Kalache and Silas Mugambi.

---
