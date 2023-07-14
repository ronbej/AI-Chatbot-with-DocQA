import os
import openai
openai.api_key = ''
messages = [ {"role": "system", "content": 
              "You are a intelligent assistant."} ]

def sendResponse(message):
    messages.append(
            {"role": "user", "content": message},
        )
    chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
      
    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return(reply)

