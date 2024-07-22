from flask import Blueprint, jsonify, request
from helpers.admin_helpers import insert_inventory_user

admin_routes = Blueprint('admin_routes', __name__)

@admin_routes.route('/add_inventory_user', methods=['GET'])
def add_inventory_user():
    insert_inventory_user()
    print("\n inserted")
    return True

