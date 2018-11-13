from flask import Flask, jsonify, request
import requests
import logging
import datetime
from valpatient import validatePatient
from valhr import validateHeartRate
app = Flask(__name__)
patientDict = {}
heartrateDict = {}
CONST_PIDKEY = "patient_id"
CONST_EMAILKEY = "attending_email"
CONST_AGEKEY = "user_age"
CONST_HRKEY = "heart_rate"
CONST_DTK = "datetime"

@app.route("/api/new_patient", methods=["POST"])
def createPatient():
    """
    Receives info, validates, overwrites existing or adds new entry

    :returns: message describing its success
    """
    r = request.get_json()
    if(validatePatient(r) == -1):
        return "invalid input"
    patientDict[r[CONST_PIDKEY]] = {CONST_EMAILKEY: r[CONST_EMAILKEY],
                                    CONST_AGEKEY: r[CONST_AGEKEY]}
    heartrateDict[r[CONST_PIDKEY]] = []
    return "Patient Added"


@app.route("/api/heart_rate", methods=["POST"])
def addHR():
    """
    Receives patient id, Heart rate, adds values to heartrateDict

    :returns: message describing its success
    """
    r = request.get_json()
    if(validateHeartRate(r, patientDict) == -1):
        return "invalid input"
    heartrateDict[r[CONST_PIDKEY]].append({CONST_DTK: datetime.datetime.now(),
                                           CONST_HRKEY: r[CONST_HRKEY]})
    return "Heart Rate Added"



if __name__ == "__main__":
    logging.basicConfig(filename='server.log', level=logging.INFO,
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info("Starting New Log...")
    app.run(host="127.0.0.1")
