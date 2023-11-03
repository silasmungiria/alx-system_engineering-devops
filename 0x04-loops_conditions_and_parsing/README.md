# 0x04. Loops, conditions, and parsing

This project covers the concepts of loops, conditions, and parsing in the context of shell scripting using Bash. It is a part of the DevOps curriculum at ALX School.

## Learning Objectives

By the end of this project, you should be able to:

- Explain the process of creating SSH keys
- Understand the advantages of using `#!/usr/bin/env bash` over `#!/bin/bash`
- Use while, until, and for loops effectively
- Implement if, else, elif, and case condition statements
- Utilize the cut command for string manipulation
- Understand file test operators and other comparison operators

## Requirements

- Allowed editors: vi, vim, emacs
- All files should be interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- A `README.md` file is mandatory at the root of the project directory
- All Bash script files must be executable
- You are not allowed to use awk
- Your Bash scripts must pass Shellcheck (version 0.7.0) without any errors
- The first line of all Bash scripts should be `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining the script's purpose

## Tasks

The project consists of the following tasks:

### 0. Create a SSH RSA key pair

- Generate a SSH RSA key pair.
- Share the public key (`0-RSA_public_key.pub`) in the answer file.
- Fill the SSH public key field of your intranet profile with the generated public key.

### 1. For Best School loop

- Write a Bash script that displays "Best School" 10 times using a `for` loop.

### 2. While Best School loop

- Write a Bash script that displays "Best School" 10 times using a `while` loop.

### 3. Until Best School loop

- Write a Bash script that displays "Best School" 10 times using an `until` loop.

### 4. If 9, say Hi!

- Write a Bash script that displays "Best School" 10 times but prints "Hi" instead of "Best School" on the 9th iteration using a `while` loop and an `if` statement.

### 5. 4 bad luck, 8 is your chance

- Write a Bash script that loops from 1 to 10 and displays different messages based on the iteration count using a `while` loop and `if`, `elif`, and `else` statements.

### 6. Superstitious numbers

- Write a Bash script that displays numbers from 1 to 20 and displays different messages for specific iterations using a `while` loop and a `case` statement.

### 7. Clock

- Write a Bash script that displays the time from 0 to 12 hours and 1 to 59 minutes using a `while` loop.

### 8. For ls

- Write a Bash script that lists the content of the current directory in a specific format using a `for` loop.

### 9. To file, or not to file

- Write a Bash script that provides information about the existence and properties of a file using `if` and `else` statements.

### 10. FizzBuzz

- Write a Bash script that displays numbers from 1 to 100 with specific conditions using a `for` loop and `if`, `elif`, and `else` statements.

### 11. Read and cut (Advanced)

- Write a Bash script that displays specific information from the `/etc/pass.

### 12. Tell the story of passwd (Advanced)

- Write a Bash script that displays the content of the /etc/passwd file using a while loop and the cut command.

### 13. Let's parse Apache logs (Advanced)

- Write a Bash script that displays the visitor IP along with the HTTP status code from an Apache log file. The
log file path is passed as an argument to the script.
### 14. Dig the data (Advanced)

- Write a Bash script that makes a request to a specific URL and displays the response body. The URL is passed as
an argument to the script.
