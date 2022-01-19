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

# Medium article text

Creating a reddit bot to do your bidding 
Reddit is gold mine of knowledge. You can find information about literally anything if you stumble upon the right sub reddit. But having so much of information also means that many times, you are looking for a needle in a haystack. Its difficult to find content that you like with such a mountain of Information. Somebody once told me over a cup of casual coffee that "if to do something, if a better technology exists, then utilise it because that's how human beings progress". Needless to say I spilled my coffee and stared. But that piece of advice has helped me to overengineer a solution to this problem of curating your content on reddit. Solution I have found is - to make your own reddit bot.
"If it keeps up, man will atrophy all his limbs but the push-button finger."
- Frank Lloyd Wright, Architect
Lets get into the nitty gritty details. Before that lets christen our bot as brevity_bot.
Prerequisites
We will be using PRAW: The Python Reddit API Wrapper in python to easily communicate with reddit from out program. 
First lets create a new directory for program using terminal/command line.
mkdir brevity_bot
cd brevity_bot
Installing and configurig praw
Installing is simple through `pip`

pip install praw

After installation you need to create a `praw.ini` file in your local directory. This `praw.ini` file is used to set configurations so that praw can communicate with your reddit account. Below code will create a ini file with an empty line in it, in windows.
echo.> praw.ini
people following along in linux can use touch command.
touch praw.ini
You can get configuration information of what to put in the `praw.ini` file from here. Or you can copy from below and instead put in your own values.

if you look at the last section of the file you'll find a block `[brevity_bot]`. brevity bot is the name of our bot. Below that you'll see fields like `client_id` and `client_secret`. For getting these values you need to register an app on reddit developer page. 
Registering your app on reddit for development
go to https://www.reddit.com/prefs/apps.
click on `create app` way down at the bottom of the page.
use the script radio button to signify that you want to run a script

choose script option4. You'll get a secret and id for your app. Put those values and credentials in the `praw.ini` file. 
5. For you bot to interact with reddit (for example reply) you need to give `praw.ini` your reddit `username` and `password` too.
Creating a reddit subreddit to test (optional)
In order for you test your bot in peace without reddit banning you its highly recommended that you create your own subbreddit from reddit. 
However if you are just following along the tutorial then I've have already made a subreddit at https://www.reddit.com/r/botjungle/. The code below uses that subreddit.
Coding the actual program in python
lets create a python file for the program. On windows-
echo.> brevity_bot.py
on linux again (`touch brevity_bot.py`)
Type the following code in brevity_bot.py

brevity bot is happy to have found a goolge colab notebook shared.First step is importing all libraries - `praw`, `os` (for file operations), `re` (for regex matching)
We initialise the praw with the bot name. The bot name is the same as the one you gave in praw.ini. Subreddit is the subreddit where the bot will go.
Our bot will be looking at the top 5 new subbreddit post. This is done by iterating over `subbreddit.hot(limit=5)`. This limit tells how many post it will look through. Be careful not to increase it too much. While looking at posts we need make sure the bot doesn't reply to same posts again and again. So we created posts_replied_to.txtto keep track of all post already replied to.
Once we find a particular text in the post, we use `submission.reply` for a reply.

Our next step should be to save these posts contents somewhere. For the code for saving the post and full code check-
https://github.com/fanbyprinciple/brevity_bot_reddit
Conclusion
And thats it! you have coded a bot for reddit which will work for you. Hope you had fun.