# 0x17. Web Stack Debugging #3

## Project Description

This project focuses on debugging a Wordpress website running on a LAMP stack. The task involves using `strace` to identify the root cause of an Apache 500 error and subsequently automating the fix using Puppet.

## Table of Contents

- [Concepts](#concepts)
- [Requirements](#requirements)
- [Tasks](#tasks)
- [Usage](#usage)
- [Author](#author)

## Concepts

- Web Server
- Web stack debugging

## Requirements

- All files will be interpreted on Ubuntu 14.04 LTS.
- All files should end with a new line.
- A `README.md` file at the root of the folder of the project is mandatory.
- Puppet manifests must pass `puppet-lint version 2.1.1` without any errors.
- Puppet manifests must run without error.
- Puppet manifests files must end with the extension `.pp`.
- Files will be checked with Puppet v3.4.

## Tasks

### 0. Strace is your friend (mandatory)

Using `strace`, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet.

**Hint:**
- `strace` can attach to a currently running process.
- You can use `tmux` to run `strace` in one window and `curl` in another one.

**Example:**
```bash
$ curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
...

$ puppet apply 0-strace_is_your_friend.pp
...
