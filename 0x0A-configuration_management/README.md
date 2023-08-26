# 0x0A Configuration Management Project

This project covers various tasks related to Configuration Management, DevOps, SysAdmin, Scripting, and CI/CD. The tasks involve working with Puppet, a popular configuration management tool, to automate various system administration tasks.

## Background Context

During their time at SlideShare, the author worked on an auto-remediation tool called Skynet that monitored, scaled, and fixed Cloud infrastructure. The project involved using a parallel job-execution system called MCollective, which allowed executing commands to one or multiple servers simultaneously. A bug in their code led to a significant incident, demonstrating the importance of proper configuration management tools like Puppet.

## Resources

- [Intro to Configuration Management](#https://intranet.alxswe.com/rltoken/GL30hu-aRcKzPOvK8JO-Bg)
- [Puppet resource type: file](#https://intranet.alxswe.com/rltoken/WON0M4DNRabf88KAG_pDUA)
- [Puppet’s Declarative Language](#https://intranet.alxswe.com/rltoken/0V2fBdafkfKPMxA1umea3Q)
- [Puppet lint](#https://intranet.alxswe.com/rltoken/CRUMeEMdcX-UtbWsUM9xLQ)
- [Puppet emacs mode](#https://intranet.alxswe.com/rltoken/MzHXCntAkPzOqMnI6_rpWQ)

## Requirements

- All files will be interpreted on Ubuntu 20.04 LTS.
- Files should end with a new line.
- A `README.md` file at the root of the project folder is mandatory.
- Puppet manifests must pass `puppet-lint` version 2.1.1 without errors.
- Puppet manifests must run without error.
- Puppet manifest files must end with the extension `.pp`.
- The Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

## Installation

To install Puppet and puppet-lint, follow these steps:

```bash
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
$ gem install puppet-lint
```

## Tasks

1. [Create a file](./0-create_a_file.pp)
    - Using Puppet, create a file in `/tmp` with specific permissions, owner, group, and content.

2. [Install a package](./1-install_a_package.pp)
    - Using Puppet, install the Flask package from pip3 with a specific version.

3. [Execute a command](./2-execute_a_command.pp)
    - Using Puppet's `exec` resource, create a manifest to terminate a process named `killmenow`.

## Author

Project by Sylvain Kalache and Silas Mugambi.

---
