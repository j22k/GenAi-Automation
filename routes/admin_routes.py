import logging
from flask import Blueprint, jsonify, request
from helpers.admin_helpers import insert_inventory_user,insert_doctor_user,insert_op_user,insert_nurse_user

admin_routes = Blueprint('admin_routes', __name__)


@admin_routes.route('/add_inventory_user', methods=['POST'])
def add_inventory_user():
    try:
        data = request.get_json()  
        # Check if data is provided
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        print(data)
        if data["password"] == data["confirmpassword"]:
            # Call the function to process or store the data
            result = insert_inventory_user(data)
            if result["status"]:
                print(result)
                return jsonify(result), 201
            else :
                return jsonify(result), 409 
        else:
            return jsonify({"message" : "Password not match"}),400
            
        
    
    except Exception as e:
        # Handle exceptions and return an error response
        print(f"An error occurred: {e}")  # For debugging
        return jsonify({'error': 'An internal error occurred'}), 500


@admin_routes.route('/add_doctor_user', methods=['POST'])
def add_doctor_user():
    try:
        data = request.get_json()  
        print(f"Received data: {data}") 
        # Check if data is provided
        if data["password"] == data["confirmpassword"]:
            # Call the function to process or store the data
            result = insert_doctor_user(data)
            if result["status"]:
                print(result)
                return jsonify(result), 201
            else :
                return jsonify(result), 409 
        else:
            return jsonify({"message" : "Password not match"}),400
    
    except Exception as e:
        # Handle exceptions and return an error response
        print(f"An error occurred: {e}")  # For debugging
        return jsonify({"status" : False,'message': 'An internal error occurred'}), 500


@admin_routes.route('/add_op_user', methods=['POST'])
def add_op_user():
    try:
        data = request.get_json()  
        # Check if data is provided
        print(data)
        if data["password"] == data["confirmpassword"]:
            # Call the function to process or store the data
            result = insert_op_user(data)
            if result["status"]:
                print(result)
                return jsonify(result), 201
            else :
                return jsonify(result), 409 
        else:
            return jsonify({"message" : "Password not match"}),400
    
    except Exception as e:
        # Handle exceptions and return an error response
        print(f"An error occurred: {e}")  # For debugging
        return jsonify({"status" : False,'message': 'An internal error occurred'}), 500
    
@admin_routes.route('/add_nurse_user', methods=['POST'])
def add_nurse_user():
    try:
        data = request.get_json()  
        logging.debug(data)
        # Check if data is provided
        print(data)
        if data["password"] == data["confirmpassword"]:
            # Call the function to process or store the data
            result = insert_nurse_user(data)
            if result["status"]:
                print(result)
                return jsonify(result), 201
            else :
                return jsonify(result), 409 
        else:
            return jsonify({"message" : "Password not match"}),400
    
    except Exception as e:
        # Handle exceptions and return an error response
        print(f"An error occurred: {e}")  # For debugging
        return jsonify({"status" : False,'message': 'An internal error occurred'}), 500



