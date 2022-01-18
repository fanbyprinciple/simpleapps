import praw
import os
import re
import re

reddit = praw.Reddit('jupyter_bot')
# subreddit = reddit.subreddit("botjungle")
# subreddit = reddit.subreddit("GoogleColabNotebooks")
subreddit = reddit.subreddit("MachineLearning")


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

if not os.path.isfile("posts_text.txt"):
    posts_text = []
else:
    with open("posts_text.txt", "r") as f:
       posts_text = f.read()
    #    posts_text =  [ "\n--------------------------------\n" + x + "\n--------------------------------\n" for x in posts_text.split("\n--------------------------------\n")]
       posts_text = posts_text.split("\n--------------------------------\n")[1:-1]
       posts_text = list(filter(None, posts_text ))


for submission in subreddit.new(limit=5):
    print("Looking at : ", submission.title)
    if submission.id not in posts_replied_to:
        if re.search("colab.research.google.com", submission.selftext, re.IGNORECASE) or re.search("google-colab.com", submission.selftext, re.IGNORECASE):
            submission.reply("jupter_bot: Thank you for sharing this Notebook. I will save it.")
            print("Bot replying to : ", submission.title)
            posts_replied_to.append(submission.id)
            posts_text.append(submission.title + " : \n" + submission.selftext )

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")

with open("posts_text.txt", "w") as f:
    for post_text in posts_text:
        f.write( "\n--------------------------------\n" + post_text + "\n--------------------------------\n")