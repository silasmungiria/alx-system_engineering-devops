# 0x06. Regular expression

This project focuses on regular expressions (regex) using the Oniguruma library, which is the default regex library for Ruby.

## Table of Contents
- [Background Context](#background-context)
- [Resources](#resources)
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [Task 0: Simply matching School](#task-0-simply-matching-school)
  - [Task 1: Repetition Token #0](#task-1-repetition-token-0)
  - [Task 2: Repetition Token #1](#task-2-repetition-token-1)
  - [Task 3: Repetition Token #2](#task-3-repetition-token-2)
  - [Task 4: Repetition Token #3](#task-4-repetition-token-3)
  - [Task 5: Not quite HBTN yet](#task-5-not-quite-hbtn-yet)
  - [Task 6: Call me maybe](#task-6-call-me-maybe)
  - [Task 7: OMG WHY ARE YOU SHOUTING?](#task-7-omg-why-are-you-shouting)
  - [Task 8: Textme](#task-8-textme)

## Background Context

In this project, you will work with regular expressions using the Oniguruma library, which is the default regular expression library for Ruby. It is important to note that other regular expression libraries might have different properties.

To get started, you will use the given Ruby code and replace the "regexp" part with your own regular expressions. The Ruby script accepts one argument and passes it to a regular expression matching method.

## Resources

Before starting this project, you should read or watch the following resources:

- [Regular expressions - basics](https://intranet.hbtn.io/rltoken/eT0zxPWmckKllzRIo4dU8Q)
- [Regular expressions - advanced](https://intranet.hbtn.io/rltoken/1CUMcsJ5rgveXN1loKXERw)
- [Rubular](https://intranet.hbtn.io/rltoken/pYtT4TkkLr1-2FgmSsDWvQ) - an online Ruby regular expression editor
- [Use a regular expression against a problem: now you have 2 problems](https://intranet.hbtn.io/rltoken/q-xcEDDIakBUIH3J0J36kw)
- [Learn Regular Expressions with simple, interactive exercises](https://intranet.hbtn.io/rltoken/Tv5NvN3N56zL2Inru6D1TA)

## Requirements

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- Your code should use the Oniguruma library
- The first line of all your Ruby scripts should be exactly `#!/usr/bin/env ruby`
- All your regex must be built for the Oniguruma library

## Tasks

### Task 0: Simply matching School

Write a Ruby script that accepts one argument and passes it to a regular expression matching method. The regular expression must match the word "School".

**Example:**
```script
$ ./0-simply_match_school.rb School | cat -e
School$
$ ./0-simply_match_school.rb "Best School" | cat -e
School$
$ ./0-simply_match_school.rb "School Best

School" | cat -e
SchoolSchool$
$ ./0-simply_match_school.rb "Grace Hopper" | cat -e
$
```


### Task 1: Repetition Token #0

Write a Ruby script that accepts one argument and passes it to a regular expression matching method. The regular expression must match the following cases:
- htn repeated one or more times

**Example:**
```script
$ ./1-repetition_token_0.rb htn | cat -e
htn$
$ ./1-repetition_token_0.rb htnhtn | cat -e
htnhtn$
$ ./1-repetition_token_0.rb htnhtnhtn | cat -e
htnhtnhtn$
$ ./1-repetition_token_0.rb hbn | cat -e
$
```

### Task 2: Repetition Token #1

Write a Ruby script that accepts one argument and passes it to a regular expression matching method. The regular expression must match the following cases:
- hbtn repeated zero or more times

**Example:**
```script
$ ./2-repetition_token_1.rb hbtn | cat -e
hbtn$
$ ./2-repetition_token_1.rb hbtntv | cat -e
hbtntv$
$ ./2-repetition_token_1.rb hbtntvhbtn | cat -e
hbtntvhbtn$
$ ./2-repetition_token_1.rb hb | cat -e
$
```

### Task 3: Repetition Token #2

Write a Ruby script that accepts one argument and passes it to a regular expression matching method. The regular expression must match the following cases:
- hbtn repeated one or more times, but not hbttn

**Example:**
```script
$ ./3-repetition_token_2.rb hbttn | cat -e
$
$ ./3-repetition_token_2.rb hbtn | cat -e
hbtn$
$ ./3-repetition_token_2.rb hbttnhbtn | cat -e
hbtn$
$ ./3-repetition_token_2.rb hbbtn | cat -e
$
```

### Task 4: Repetition Token #3

Write a Ruby script that accepts one argument and passes it to a regular expression matching method. The regular expression must match the following cases:
- hbn followed by any single character, except b

**Example:**
```script
$ ./4-repetition_token_3.rb hbn | cat -e
hbn$
$ ./4-repetition_token_3.rb hbon | cat -e
hbon$
$ ./4-repetition_token_3.rb hbtn | cat -e
$
$ ./4-repetition_token_3.rb hbtnhbn | cat -e
hbn$
```

### Task 5: Not quite HBTN yet

Write a Ruby script that accepts one argument and passes it to a regular expression matching method. The regular expression must match a string that starts with h, ends with n, and can have any single character in between.

**Example:**
```script
$ ./5-beginning_and_end.rb 'hn' | cat -e
$
$ ./5-beginning_and_end.rb 'hbn' | cat -e
hbn$
$ ./5-beginning_and_end.rb 'hbtn' | cat -e
$
$ ./5-beginning_and_end.rb 'h8n' | cat -e
h8n$
```

### Task 6: Call me maybe

Write a Ruby script that accepts one argument and passes it to a regular expression matching method. The regular expression must match a 10-digit phone number.

**Example:**
```script
$ ./6-phone_number.rb 4155049898 | cat -e
4155049898$
$ ./6-phone_number.rb " 4155049898" | cat -e
$
$ ./6-phone_number.rb "415 504 9898" | cat -e
$
$ ./6-phone_number.rb "415-504-9898" | cat -e
$
```

### Task 7: OMG WHY ARE YOU SHOUTING?

Write a Ruby script that accepts one argument and passes it to a regular expression matching method. The regular expression must match only capital letters.

**Example:**
```script
$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e
ILOVESYSADMIN$
$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e
WHATSAY$
$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e
$
```

### Task 8: Textme (Advanced)

Write a Ruby script that accepts one argument and passes it to a regular expression matching method. The regular expression must extract the sender, receiver, and flags from the given log line.

**Example:**
```script
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-0-11 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE1] [SVC:] [ACT:] [BINF:] [FID:] [from:Google] [to:+16474951758] [flags:-1:0:-1:0:-1] [msg:127:This planet has - or rather had - a problem, which was this: most of the people on it were unhappy for pretty much of the time.] [udh:0:]'
Google,+16474951758,-1:0:-1:0:-1
$
$ ./100-textme.rb 'Feb 1 11:00:00 ip-10-0-64-10 mdr: 2016-02-01 11:00:00 Receive SMS [SMSC:SYBASE2] [SVC:] [ACT:] [BINF:] [FID:] [from:+17272713208] [to:+19172319348] [flags:-1:0:-1:0:-1] [msg:136:Orbiting this at a distance of roughly"```
```
