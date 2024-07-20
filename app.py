from flask import Flask, render_template, request, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def dummy():
    function_sign_in = [
        {'arguments': {'username': 'user@123', 'password': 'user@123'}, 'name': 'Sign_in'}
    ]
    item = function_sign_in[0]
    name = item['name']
    arguments = item['arguments']
    Username = arguments['username']
    Password = arguments['password']
    return Username, Password, name

val = dummy()

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/sign_in', methods=['POST'])
def signin():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    logging.debug(f"Username: {username}, Password: {password}")

    response = {"status": "success", "message": "Sign-in successful"}
    return jsonify(response)

@app.route('/send_message', methods=['POST'])
def send_message():
    
    data = request.get_json()
    msg = data.get('msg')
    # Directly call sign-in logic
    username, password, name = val
    # You can replace this with actual sign-in logic
    sign_in_response = {"status": "success", "message": "Sign-in successful"}  # Mock response

    # import requests
    # response = requests.post('http://127.0.0.1:5000/sign_in', json={'username': val[0], 'password': val[1]})

    logging.debug(f"Sign-in response: {sign_in_response}")
    logging.debug(f"Received message: {msg}")

    return jsonify({"status": "success", "message": "Message received!"})

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
