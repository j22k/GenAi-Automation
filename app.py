from flask import Flask, render_template, request, jsonify, url_for
import logging
from config.connection import get_db
from config.collections import Collection
from routes.admin_routes import admin_routes
from function_calling import functons_background

functions_instance = functons_background()

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize database connection
db_connection = get_db()
if db_connection["status"] == "error":
    logging.error(f"Database connection failed: {db_connection['message']}")
else:
    logging.info("Database connection established successfully.")

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
    if request.is_json:
            data = request.get_json()
            response = functons_background.log_in(data["username"],data["password"])
            return jsonify({'message': 'Login successful', 'data': data}), 200
    else:
            return jsonify({'error': 'Unsupported Media Type'}), 415
   

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
