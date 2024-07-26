import requests
import logging
from function_calling import functons_background
from config.config import GROQ_API
from groq import Groq

# Configure logging
logging.basicConfig(level=logging.DEBUG)

client = Groq(
    api_key=GROQ_API,
)

functions_instance = functons_background()



functions_name = ("Sign_in")
functions = {
    "Sign_in" : (functons_background.log_in,("value1","value2"))
}

model_name="llama3-70b-8192"
system_prompt = {
    "role": "system",
    "content":
    "You are a helpful assistant for a hospital management system your name is LIFEbot. You reply with very precise small answers."
    }
chat_history = [system_prompt]

class chat:
    
    def chat_with_message(self, message):
        try:

            chat_history.append({"role": "user", "content": message})

            chat_completion = client.chat.completions.create(model=model_name,
                                            messages=chat_history,
                                            max_tokens=100,
                                            temperature=1.2
        )
            print(f"\n\n{chat_completion}\n\n")
            print(f"\n\n{chat_completion.choices[0].message.content}\n\n")
            return ({"response_message" : chat_completion.choices[0].message.content})
        
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            return {"status": "error", "message": "HTTP error occurred"}
        except requests.exceptions.RequestException as req_err:
            logging.error(f"Request failed: {req_err}")
            return {"status": "error", "message": "Request failed"}
        
def switch_case(message):
    if message[2] == "Sign_in":
        return functons_background.log_in(message[0],message[1])

def find_matching_function(functions_name, target_function):
    if target_function in functions_name:
        return target_function
    else:
        print(f"The value {target_function} is not present in the list.")