import logging
from flask import Blueprint, jsonify, request,render_template,session
from helpers.doctor_helpers import getappointmentsHelpers

doctor_routes = Blueprint('doctor_routes', __name__, template_folder='templates')

@doctor_routes.route('/home')
def home():
    appointmentsoTaday = getappointmentsHelpers()
    
    logging.debug(f"\n\n\nAppointments data: {appointmentsoTaday}")
    logging.debug(f"\n\n\nLength of data: {len(appointmentsoTaday)}")
    logging.debug(f"\n\n\nType of data: {type(appointmentsoTaday)}")
    
    return render_template('doctor/home.html', appointments=appointmentsoTaday)
