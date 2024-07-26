from helpers.op_helpers import addpatientHelpers
import logging
from flask import Blueprint, jsonify, request,render_template

op_routes = Blueprint('op_routes', __name__, template_folder='templates')

@op_routes.route('/home')
def admin_home():
    full_url = request.url
    args = request.args
    user_id = args.get('id', 'Not Provided')
    name = args.get('name', 'Not Provided')
    user_type = args.get('userType', 'Not Provided')
    return render_template('op/home.html', user_id=user_id, name=name, user_type=user_type)


@op_routes.route('/patient_registration', methods=['POST'])
def op_patient_registration():
    data = request.get_json()
    logging.debug("Received data: %s", data)
    response = addpatientHelpers(data)
    logging.debug("Response: %s", response)
    return jsonify(response)
