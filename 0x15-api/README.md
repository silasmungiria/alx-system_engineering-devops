# 0x15. API

This project revolves around working with APIs using Python. It emphasizes the importance of APIs in modern system administration and the advantages they offer over traditional Bash scripting for certain tasks.

## Background Context

Traditionally, system administrators relied heavily on Bash scripting. However, this project highlights that for more complex and efficient operations, modern administrators, often called SREs, employ a wider range of programming languages, with Python being a significant choice. APIs play a vital role in exposing applications and datasets to interact with external sources.

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without consulting external resources:

- The limitations of Bash scripting.
- What an API is.
- What a REST API is.
- What microservices are.
- Understanding of CSV and JSON formats.
- Pythonic style for package, module, class, variable, function, and constant names.

## Requirements

### General

- Allowed editors: vi, vim, emacs.
- Code to be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).
- All files must end with a new line.
- The first line of all files should be exactly `#!/usr/bin/python3`.
- Organize imported libraries in alphabetical order.
- A `README.md` file at the root of the project folder is mandatory.
- Code should be compliant with `pycodestyle` (version 2.8.*).
- All files must be executable.
- Length of files will be tested using `wc`.
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
- Use `get` to access dictionary values by key (no exception if key doesn't exist).
- Code should not execute when imported (`if __name__ == "__main__":`).

## Tasks Overview

### 0. Gather data from an API

Write a Python script that, using a specific REST API, fetches and displays information about a given employee's TODO list progress.

### 1. Export to CSV

Extend the previous script to export data in CSV format, recording all tasks owned by the employee.

### 2. Export to JSON

Further extend the original script to export data in JSON format, adhering to a specific format.

### 3: Dictionary of List of Dictionaries

Task 3 builds upon the previous tasks. It requires extending the Python script to export data in the JSON format. The script should now record tasks from all employees and format the data as a dictionary of lists of dictionaries. Each user's tasks are grouped under their respective user ID, and each task is represented by a dictionary containing information like username, task title, and completion status. The output file should be named todo_all_employees.json.

---
