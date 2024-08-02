import logging
from flask import Blueprint, jsonify, request,render_template,session
from helpers.doctor_helpers import getappointmentsHelpers

doctor_routes = Blueprint('doctor_routes', __name__, template_folder='templates')

@doctor_routes.route('/home')
def home():
    args = request.args
    user_id = args.get('id', 'Not Provided')
    name = args.get('name', 'Not Provided')
    user_type = args.get('userType', 'Not Provided')
    appointmestToaday = getappointmentsHelpers()
    return render_template('doctor/home.html', user_id=user_id, name=name, user_type=user_type, apointments=appointmestToaday)

