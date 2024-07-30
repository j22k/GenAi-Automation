import logging
from flask import Blueprint, jsonify, request,render_template,session
from helpers.inventory_helpers import addnewitemHelpers,getstocklistHelpers,orderstockHelpers
from Bot import chat

chat_instance = chat()

inventory_routes = Blueprint('inventory_routes', __name__, template_folder='templates')

@inventory_routes.route('/home')
def home():
    args = request.args
    user_id = args.get('id', 'Not Provided')
    name = args.get('name', 'Not Provided')
    user_type = args.get('userType', 'Not Provided')
    return render_template('inventory/home.html', user_id=user_id, name=name, user_type=user_type)


@inventory_routes.route('/add_new_stock', methods=['POST'])
def add_new_stock():
    
    data = request.get_json()  
    logging.debug(data)
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    logging.debug(session["user"] == "inventory")
    if (session["user"] == "inventory"):
        logging.debug(f"\n\n\n 1 {session}")
        response = addnewitemHelpers(data)
        return response
    elif(session["user"] == "admin"):
        logging.debug(f"\n\n\n 1 {session}")
        response = addnewitemHelpers(data)
        return response
    else:
        return {"status": False, "message": "Sorry, You dont have access!!"}
    
@inventory_routes.route('/get_stock_list', methods=['GET'])
def get_stock_list():
    
    if (session["user"] == "inventory" or session["user"] == "admin"):
        return jsonify(getstocklistHelpers())
    
    else:
        return {"status": False, "message": "Sorry, You dont have access!!"}
    
@inventory_routes.route('/order_item', methods=['POST'])
def order_item():
    itemID = request.get_json()
    logging.debug(f"\n\n{itemID}\n\n")  
    if (session["user"] == "inventory" or session["user"] == "admin"):
        itemdetails = orderstockHelpers(itemID)
        del itemdetails["_id"]
        del itemdetails["description"]
        del itemdetails["quantity"]
        del itemdetails["purchaseDate"]
        del itemdetails["location"]
        del itemdetails["expirationDate"]
        del itemdetails["cost"]
        del itemdetails["batchNumber"]
        logging.debug(f"\n\n just looking\n\n")
        draft_mail  =  chat_instance.draft_mail_for_oder(itemdetails)
        
        return {"mail" : draft_mail, "status" : True}
    
    else:
        return {"status": False, "message": "Sorry, You dont have access!!"}