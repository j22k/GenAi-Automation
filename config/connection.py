# config/connection.py
import pymongo

def db_connect():
    try:
        # Create a MongoClient instance to connect to MongoDB
        myclient = pymongo.MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=5000)
        
    
        # Select the database
        db = myclient["GenAi_automation"]
        return {
            "status": "success",
            "message": f"Successfully connected to MongoDB and selected database'",
            "db": db
        }
    except ConnectionError as e:
        return {
            "status": "error",
            "message": f"MongoDB connection error: {str(e)}"
        }
    