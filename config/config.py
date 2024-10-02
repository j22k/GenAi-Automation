import os
GROQ_API = "replace with your api key"

class Config:
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'default_secret_key')
