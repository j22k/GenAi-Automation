import os
from config.config import GROQ_API
from groq import Groq


# Create the Groq client
client = Groq(api_key=GROQ_API)

# Set the system prompt
system_prompt = {
    "role": "system",
    "content": """
    You are a helpful assistant. You reply with json response which extract from user prompt you have access to:
    {
        "name": "login",
        "description": "Login a user with username and password",
        "parameters": {
            "properties": {
                "username": {
                    "description": "The username for login",
                    "type": "string"
                },
                "password": {
                    "description": "The password for login",
                    "type": "string"
                }
            },
            "required": [
                "username",
                "password"
            ],
            "type": "object"
        }
    },
    {
        "name": "getstock",
        "description": "Get the current stock for a given item",
        "parameters": {
            "properties": {
                "itemname": {
                    "description": "The name of the item to check stock for",
                    "type": "string"
                }
            },
            "required": [
                "itemname"
            ],
            "type": "object"
        }
    },
    {
        "name": "notfound",
        "description": "Response when the requested command is not found",
        "parameters": {
            "properties": {
                "message": {
                    "description": "The error message",
                    "type": "string"
                }
            },
            "required": [
                "message"
            ],
            "type": "object"
        }
    }
    """
}

# Initialize the chat history
chat_history = [system_prompt]

while True:
    # Get user input from the console
    user_input = input("You: ")

    # Append the user input to the chat history
    chat_history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=chat_history,
        max_tokens=100,
        temperature=1.2
    )

    # Append the response to the chat history
    chat_history.append({
        "role": "assistant",
        "content": response.choices[0].message.content
    })

    # Print the assistant's response
    print("Assistant:", response.choices[0].message.content)