from random import choice

import os
import openai 

from credentials import openai_key

#https://beta.openai.com/account/api-keys


openai.api_key = openai_key["key"]
completion = openai.Completion()

start_sequence = '\nfanbot:'
restart_sequence = '\n\nyou:'

f1 = open('extracted_tanu_whatsapp.txt', 'r+', encoding='UTF-8')
session_prompt = f1.readlines()

session_prompt = session_prompt[0:2100]
#print(session_prompt)
print("length of session prompt: ", len(session_prompt), '. Open ai bot initialised.')

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


def call_bot():
    while(1):
        input_text = input("You: ")
        incoming_msg = input_text
        answer = ask(incoming_msg, session_prompt)
        session_prompt = append_interaction_to_chat_log(incoming_msg, answer, session_prompt)
        print(f"fanbot: {answer}")

if __name__ == 'main':
    call_bot()
