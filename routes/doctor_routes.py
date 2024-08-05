import logging
from flask import Blueprint, render_template
from helpers.doctor_helpers import getappointmentsHelpers,getPatient

doctor_routes = Blueprint('doctor_routes', __name__, template_folder='templates')

@doctor_routes.route('/home')
def home():
    appointmentsoTaday = getappointmentsHelpers()
    
    logging.debug(f"\n\n\nAppointments data: {appointmentsoTaday}")
    logging.debug(f"\n\n\nLength of data: {len(appointmentsoTaday)}")
    logging.debug(f"\n\n\nType of data: {type(appointmentsoTaday)}")
    
    return render_template('doctor/home.html', appointments=appointmentsoTaday)


@doctor_routes.route('/diagnosis/<patient_id>')
def diagnosis(patient_id):
    logging.debug(f"\n\n {patient_id} \n\n")

    response = getPatient(patient_id)
    
    logging.debug(f"\n\n {response} \n\n")
    # if not patient:
    #     return {"status": False, "response_message": "Patient not found"}
    
    # Render a template for diagnosis or handle the diagnosis logic
    return render_template('doctor/doc_diagnosis.html',patient=response)
