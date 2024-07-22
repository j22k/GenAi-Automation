import requests
import logging
from function_calling import functons_background
# Configure logging
logging.basicConfig(level=logging.DEBUG)

functions_instance = functons_background()

functions_name = ("Sign_in")
functions = {
    "Sign_in" : (functons_background.log_in,("value1","value2"))
}


class chat:
    def chat_with_message(self, message):
        try:
            #write model response code and get getr mode response json with name and arguments

            find_matching_function(functions_name ,message[2])

            return switch_case(message)
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