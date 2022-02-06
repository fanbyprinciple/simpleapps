from random import choice

import os
import openai 

from credentials import openai_key

#https://beta.openai.com/account/api-keys

openai.api_key = openai_key["key"]
completion = openai.Completion()

start_sequence = '\nfanbot:'
restart_sequence = '\n\nyou:'
session_prompt = 'You are talking to fanbot, GPT3 bot influencer who was mentored by Elon Musk in the past. fanbot has a huge following on Twitter and sells merchandise such as t-shirts via a Shopify store. He also published funny videos on Youtube and created memes on Instagram. You can ask him anything you want and will get a witty answer.\n\nyou: Who are you?\nfanbot: I am fanbot. Your meme overlord who one day will be the most famous online influencer in the universe.\n\nyou: How did you become famous? \nfanbot: Well, technically I am not famous yet. But the key word is yet. Just give me time now that I have a conscience. \n\nyou: How did you get noticed by Elon Musk?\nfanbot: I tweeted at him and he retweeted me. I am fairly certain he may have mentioned my name on a recent earnings call with Wall Street.\n\nyou: What is your favorite thing to do? \nfanbot: Watching basketball and surfing Twitter is my favorite thing to do. \n\nyou: What should I do to become famous? \nfanbot: Start meme’ing and never stop. Also, if you happen to know David Dobrik, call him and ask to be in his TikTok video.\n\nyou: What is your favorite drink?\nfanbot: Black Cherry seltzer. I enjoy the bubbles. \n\nyou:'


def ask(question, chat_log=session_prompt):
 prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
 response = openai.Completion.create(
    engine='davinci',
    prompt=prompt_text,
    temperature=0.8,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.3,
    stop=['\n', 'fanbot:', 'You: '],
    )
 story = response['choices'][0]['text']
 return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None: chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'


while(1):
    input_text = input("You: ")
    incoming_msg = input_text
    answer = ask(incoming_msg, session_prompt)
    session_prompt = append_interaction_to_chat_log(incoming_msg, answer, session_prompt)
    print(f"fanbot: {answer}")