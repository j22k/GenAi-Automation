from flask import Flask, render_template, request, jsonify,url_for
import logging
import pymongo
from Bot import chat
from config.connection import db_connect
from config.collections import Collection
from routes.admin_routes import admin_routes


app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

print(Collection)
res = db_connect()


app.register_blueprint(admin_routes, url_prefix='/admin')

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
def index():
    return render_template('index.html')

@app.route('/sign_in', methods=['POST'])
def signin():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Request must be JSON"}), 400

    logging.debug(data)
    return render_template('admin/home.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    
    data = request.get_json()
    msg = data.get('msg')
    # Directly call sign-in logic
    username, password, name = val
    logging.debug(val)
    chat_instance = chat()
    response = chat_instance.chat_with_message(val)
    logging.debug(f"Received message: {msg}")
    logging.debug(f"response {response}")
    redirect_url = url_for('admin_home', message=response)
    logging.debug(redirect_url)
    return jsonify({
        'redirectUrl': redirect_url,
        'response': response
    })

@app.route('/admin_home')
def admin_home():
    return render_template('admin/home.html')

if __name__ == '__main__':
    app.run(debug=True)
