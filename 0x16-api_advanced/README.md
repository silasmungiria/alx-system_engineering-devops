# 0x16. API Advanced

## Project Description
This project is part of the ALX Software Engineering program and focuses on working with APIs, specifically the Reddit API. It involves tasks related to querying the Reddit API and performing various operations with the data obtained. The goal is to improve your skills in using APIs and processing their data.

## Background Context
Questions involving APIs are common for interviews. Sometimes they’re as simple as ‘write a Python script that queries a given endpoint’, sometimes they require you to use recursive functions and format/sort the results.

A great API to use for some practice is the Reddit API. There’s a lot of endpoints available, many that don’t require any form of authentication, and there’s tons of information to be parsed out and presented. Getting comfortable with API calls now can save you some face during technical interviews and even outside of the job market, you might find personal use cases to make your life a little bit easier.

### Resources
- [Reddit API Documentation](https://www.reddit.com/dev/api/)
- [Query String](https://en.wikipedia.org/wiki/Query_string)

## Learning Objectives
By completing this project, you will gain proficiency in the following areas:

### General
- How to read API documentation to find the endpoints you’re looking for.
- How to use an API with pagination.
- How to parse JSON results from an API.
- How to make a recursive API call.
- How to sort a dictionary by value.

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3).
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/python3`.
- Libraries imported in your Python files must be organized in alphabetical order.
- A README.md file, at the root of the folder of the project, is mandatory.
- Your code should use the PEP 8 style.
- All your files must be executable.
- The length of your files will be tested using `wc`.
- All your modules should have documentation (use `python3 -c 'print(__import__("my_module").__doc__)` to check).

## Tasks
1. **How many subs?**
   - Write a function that queries the Reddit API and returns the number of subscribers for a given subreddit. If an invalid subreddit is given, the function should return 0.
   - Requirements:
     - Prototype: `def number_of_subscribers(subreddit)`
     - If not a valid subreddit, return 0.

2. **Top Ten**
   - Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
   - Requirements:
     - Prototype: `def top_ten(subreddit)`
     - If not a valid subreddit, print None.

3. **Recurse it!**
   - Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.
   - Requirements:
     - Prototype: `def recurse(subreddit, hot_list=[])`
     - If not a valid subreddit, return None.

4. **Count it! (Advanced)**
   - Write a recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces).
   - Requirements:
     - Prototype: `def count_words(subreddit, word_list)`
     - If no posts match or the subreddit is invalid, print nothing.

## Usage
You can run the scripts provided for each task and pass the required arguments to them.

For example:
```bash
python3 0-main.py programming
```

## Acknowledgments
This project was completed as part of the ALX Software Engineering program.
