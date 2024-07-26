
from config.connection import get_db
from config.collections import Collection
import logging

def addpatientHelpers(data):
    db_connection = get_db()
    if db_connection["status"] == "error":
        return {"status": False, "message": "Database Connection Error"}
    
    db = db_connection["db"]

    try:
        collection_name = Collection["PATIENTS"]
        if collection_name not in db.list_collection_names():
            db.create_collection(collection_name)
        collection = db[collection_name]
        # Insert the data into the collection
        result = collection.insert_one(data)
        return {"status": True, "message": "Patient added successfully", "name": data["firstname"], "user_id":str(result.inserted_id)}
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"status": False, "message": f"An error occurred: {e}"}
