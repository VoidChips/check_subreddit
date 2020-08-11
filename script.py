import praw
import sys
import auth_config as ac

reddit = praw.Reddit(client_id=ac.client_id,
                     client_secret=ac.client_secret,
                     user_agent=ac.user_agent)


# get the subreddit name from argument
subreddit_name = sys.argv[1]
number_of_post = int(sys.argv[2]) if len(sys.argv) == 3 else 2

# print hot posts from subreddit
for submission in reddit.subreddit(subreddit_name).hot(limit=number_of_post):
    print('\nshowing post\n'.upper())
    print('*' * 80)
    print(f'[{submission.score}] {submission.author}: {submission.title}\n')
    print(submission.selftext)
    print(f'\n{submission.num_comments} comments')
    print('*' * 80)

    # print the comments
    print('\nshowing comments\n'.upper())
    comments = list(submission.comments)
    for comment in comments:
        print(f'[{comment.score}] {comment.author}: {comment.body}')
        print('-' * 80)
    # print('\n')
