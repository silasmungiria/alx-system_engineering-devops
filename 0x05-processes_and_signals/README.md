echo "# 0x05. Processes and Signals

This repository contains the solutions for the \"0x05. Processes and Signals\" project, which is part of the DevOps curriculum at ALX School. The project focuses on processes and signals in Linux and Bash scripting.

## Learning Objectives

By the end of this project, you will be able to:

- Explain what a PID (Process ID) is.
- Understand the concept of a process in Linux.
- Find the PID of a process.
- Terminate a process.
- Understand the concept of signals in Linux.
- Identify the two signals that cannot be ignored.

## Requirements

- Allowed editors: vi, vim, emacs.
- All files should be interpreted on Ubuntu 20.04 LTS.
- All files should end with a new line.
- The first line of all Bash scripts should be exactly \`#!/usr/bin/env bash\`.
- The second line of all Bash scripts should be a comment explaining what the script does.
- All Bash script files must be executable.
- All Bash scripts must pass Shellcheck without any error (version 0.7.0 via apt-get).
- A README.md file, at the root of the folder of the project, is mandatory.

## Files and Directories

The project is organized as follows:

\`\`\`
alx-system_engineering-devops/
└── 0x05-processes_and_signals/
    ├── 0-what-is-my-pid
    ├── 1-list_your_processes
    ├── 2-show_your_bash_pid
    ├── 3-show_your_bash_pid_made_easy
    ├── 4-to_infinity_and_beyond
    ├── 5-dont_stop_me_now
    ├── 6-stop_me_if_you_can
    ├── 7-highlander
    ├── 8-beheaded_process
    ├── 67-stop_me_if_you_can
    ├── 100-process_and_pid_file
    ├── 101-manage_my_process
    └── 102-zombie.c
\`\`\`

### Description of Scripts

- \`0-what-is-my-pid\`: Bash script that displays its own PID.
- \`1-list_your_processes\`: Bash script that displays a list of currently running processes.
- \`2-show_your_bash_pid\`: Bash script that displays lines containing the word \"bash\" to get the PID of the Bash process.
- \`3-show_your_bash_pid_made_easy\`: Bash script that displays the PID and process name of processes containing the word \"bash\".
- \`4-to_infinity_and_beyond\`: Bash script that displays the message \"To infinity and beyond\" indefinitely with a sleep of 2 seconds between each iteration.
- \`5-dont_stop_me_now\`: Bash script that stops a process named \"my_process\" using its PID.
- \`6-stop_me_if_you_can\`: Bash script that kills a process named \"my_process\".
- \`7-highlander\`: Bash script that displays \"I am invincible!!!\" indefinitely.
- \`8-beheaded_process\`: Bash script that kills the process 98.
- \`67-stop_me_if_you_can\`: Bash script that kills a process named \"my_process\" or displays \"No process found\" if the process doesn't exist.
- \`100-process_and_pid_file\`: Bash script that creates a file named \"/var/run/my_process.pid\" containing the PID of the current process.
- \`101-manage_my_process\`: Bash script that manages the process \"my_process\" (start/stop/status).
- \`102-zombie.c\`: C program that creates 5 zombie processes.

## How to Use

1. Clone the repository:

\`\`\`bash
git clone https://github.com/mugambi12/alx-system_engineering-devops.git
\`\`\`

2. Navigate to the project directory:

\`\`\`bash
cd alx-system_engineering-devops/0x05-processes_and_signals
\`\`\`

3. Run the desired script:

\`\`\`bash
./script_name
\`\`\`

Replace \`script_name\` with the name of the script you want to execute.

## Author

This project was done by Silas Mugambi.

**Note:** This project is for educational purposes only and should not be used for plagiarism or cheating in any form.
" > README.md
