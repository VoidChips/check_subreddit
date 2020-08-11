# check_subreddit
Requirements: 
* **PRAW** library\
Install **PRAW** on linux:\
`pip3 install praw`

* **auth_config.py** file in root directory\
Replace details with your information
```
client_id = 'your client id'
client_secret = 'your client secret'
user_agent = 'your user agent'
```

How to use on linux:\
`python3 check_subreddit.py <subreddit_name> (OPTIONAL)<number_of_posts_to_show>`
