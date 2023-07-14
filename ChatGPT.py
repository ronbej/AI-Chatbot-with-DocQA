import os
import openai
openai.api_key = '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'
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

