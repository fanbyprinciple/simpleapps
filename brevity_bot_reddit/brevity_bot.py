import praw
import os
import re
import re

reddit = praw.Reddit('brevity_bot')
subreddit = reddit.subreddit("botjungle")

# for submission in subreddit.hot(limit=5):
#     print("Title: ", submission.title)
#     print("Text: ", submission.selftext)
#     print("Score: ", submission.score)
#     print("---------------------------------\n")

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
       posts_replied_to = f.read()
       posts_replied_to = posts_replied_to.split("\n")
       posts_replied_to = list(filter(None, posts_replied_to))


for submission in subreddit.hot(limit=5):
    if submission.id not in posts_replied_to:
        if re.search("Can you reply to this?", submission.title, re.IGNORECASE):
            submission.reply("brevity_bot: I wannabe!")
            print("Bot replying to : ", submission.title)
            posts_replied_to.append(submission.id)

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")