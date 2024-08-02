from flask import session
from config.connection import get_db
from datetime import datetime
import logging
from config.collections import Collection
from bson import ObjectId


def getappointmentsHelpers():
    db_connection = get_db()
    if db_connection["status"] == "error":
        return {"status": False, "response_message": "Database Connection Error"}
    
    db = db_connection["db"]
    # Assume the doctor's ID is stored in the session
    doctor_id = session.get('userID')
    logging.debug(f"\n\n {doctor_id} \n\n")
    # Get today's date in the correct format
    today_date = datetime.now().strftime('%Y-%m-%d')
    logging.debug(f"\n\n {today_date} \n\n")
    # Query to find all appointments for the doctor today
    appointments = db.appointments.find({
        'doc_id': doctor_id,
        'date': today_date
    })
    appointments_list = list(appointments)
    logging.debug(f"\n\n {appointments_list} \n\n")
    # Retrieve patient details for each appointment
    results = []
    for appointment in appointments:
        patient_id = appointment['patientId']
        patient = db.patients.find_one({'_id': patient_id})
        if patient:
            results.append({
                'appointment': appointment,
                'patient': patient
            })

    logging.debug(f"\n\n {results} \n\n")
    # Print the results
    for result in results:
        print(f"Appointment: {result['appointment']}")
        print(f"Patient: {result['patient']}")
    return True