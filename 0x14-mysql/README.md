# Project: MySQL Database Management

## Overview

This project focuses on setting up and managing a MySQL database system. It covers various tasks related to installation, user management, replication, and backup strategies.

## Learning Objectives

Upon completion of this project, you should be able to:

- Understand the role and importance of a database in a system.
- Set up a primary-replica infrastructure using MySQL for redundancy and load distribution.
- Create and manage users with specific permissions for database access.
- Perform database backups and store them in different physical locations to ensure data availability in case of server failures.

## Project Structure

The project consists of the following tasks:

### Task 0: Install MySQL

- Install MySQL 5.7.x on both `web-01` and `web-02` servers.

### Task 1: Let us in!

- Create a MySQL user named `holberton_user` on both `web-01` and `web-02` with the host set to `localhost` and password `projectcorrection280hbtn`.
- Grant `REPLICATION CLIENT` privileges to `holberton_user`.

### Task 2: If only you could see what I've seen with your eyes

- Create a database named `tyrell_corp`.
- Within `tyrell_corp`, create a table named `nexus6` and add at least one entry.

### Task 3: Quite an experience to live in fear, isn't it?

- Create a new user `replica_user` on `web-01` with host `%` and a password of your choice.
- Grant appropriate permissions to `replica_user` for replication.

### Task 4: Setup a Primary-Replica infrastructure using MySQL

- Set up replication for the MySQL database named `tyrell_corp`.
- Provide the MySQL primary configuration in the answer file `4-mysql_configuration_primary`.
- Provide the MySQL replica configuration in the answer file `4-mysql_configuration_replica`.

### Task 5: MySQL backup

- Write a Bash script that generates a MySQL dump and creates a compressed archive out of it.
- The MySQL dump must contain all databases and be named `backup.sql`.
- The compressed archive must have the format `day-month-year.tar.gz`.

## Important Notes

- Ensure that all Bash scripts are executable and pass Shellcheck.
- Follow the provided requirements for file naming, comments, and permissions.

---
