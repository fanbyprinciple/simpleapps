# Creating a brevity bot
from https://new.pythonforengineers.com/blog/build-a-reddit-bot-part-1/

1. `pip install praw`

2. created a config.py with the client ke and the secret

3. create a `praw.ini` file. check sample_praw

from : https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html#praw-ini-files

4. created a subreddit r/botjungle

5. first test at brevity_bot.py

```
(ash) PS D:\codeplay\simpleapps\brevity_bot_reddit> python .\brevity_bot.py
Title:  r/botjungle Lounge
Text:  A place for members of r/botjungle to chat with each other
Score:  1
---------------------------------

Title:  Hi welcome !
Text:  This is a test reddit for bot testing. You are welcome to use this space. Lets see how fast this place is banned.
Score:  1
---------------------------------
```

bot can also reply

```
(ash) PS D:\codeplay\simpleapps\brevity_bot_reddit> python .\brevity_bot.py
Bot replying to :  Can you reply to this?
```

6. Creating a bot to get all google colab papers

Able to extract notebooks:

run the python file and got here `https://www.reddit.com/r/botjungle`

```
https://www.reddit.com/r/botjungle/comments/s6wj2x/new_notebook_can_bot_refer_to_this/

```

7. Need to try for `r/MachineLearning`

![](colab_output.png)
