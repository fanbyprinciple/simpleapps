from random import choice

import os
import openai 
import time

from credentials import openai_key

#https://beta.openai.com/account/api-keys


openai.api_key = openai_key["key"]
completion = openai.Completion()

start_sequence = '\nfanbot:'
restart_sequence = '\n\nyou:'

# f1 = open('extracted_tanu_whatsapp.txt', 'r+', encoding='UTF-8')
# session_prompt = f1.readlines()

# session_prompt = session_prompt[0:2100]

session_prompt = """
The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.
"""
#print(session_prompt)
print("length of session prompt: ", len(session_prompt), '. Open ai bot initialised.')


chat_log = session_prompt

def ask(question):
 global chat_log
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
    if chat_log is None: 
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'

def append_to_session_prompt(question, answer):
    global session_prompt
    session_prompt += session_prompt +". you: " + question + ". fanbot: " + answer

def call_bot(session_prompt):
    while(1):
        input_text = input("You: ")
        incoming_msg = input_text
        answer = ask(incoming_msg)
        print(answer, session_prompt, incoming_msg)
        time.sleep(2)
        session_prompt = append_to_session_prompt(incoming_msg, answer)
        print(f"fanbot: {answer}")

if __name__ == 'main':
    call_bot(session_prompt)
