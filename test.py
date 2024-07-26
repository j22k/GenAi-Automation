import os
from config.config import GROQ_API
from groq import Groq

client = Groq(
    api_key=GROQ_API,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)