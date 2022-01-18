import praw
reddit = praw.Reddit('brevity_bot')
subreddit = reddit.subreddit("botjungle")


for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")