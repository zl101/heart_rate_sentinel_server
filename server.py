from flask import Flask, jsonify, request
import requests
import logging
import datetime
import numpy
from valpatient import validatePatient
from valhr import validateHeartRate
from valpid import validatePid
from istachy import checkTachy
from intervalavg import intervalAvgHelper
app = Flask(__name__)
patientDict = {}
heartrateDict = {}
CONST_PIDKEY = "patient_id"
CONST_EMAILKEY = "attending_email"
CONST_AGEKEY = "user_age"
CONST_HRKEY = "heart_rate"
CONST_DTK = "datetime"
C = "heart_rate"


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


@app.route("/api/status/<patient_id>", methods=["GET"])
def findTachy(patient_id):
    """
    given patient id, validates that hr exists, and then check tachycardic

    Returns in format 1|datetime

    :returns: 1 if tachycardic, -1 if not, 0 if error
    """
    if(validatePid(patient_id, patientDict, heartrateDict) == -1):
        return "0"
    in1 = patientDict[patient_id][CONST_AGEKEY]
    in2 = heartrateDict[patient_id][-1][CONST_HRKEY]
    arg3 = heartrateDict[patient_id][-1][CONST_DTK]
    result = checkTachy(in1, in2)
    ret = str(result) + "|" + str(arg3)
    return ret


@app.route("/api/heart_rate/<patient_id>", methods=["GET"])
def getAllHr(patient_id):
    """
    look up patient and returns all heart rates recorded

    :returns: string of all hr's
    """
    if(validatePid(patient_id, patientDict, heartrateDict) == -1):
        return "no hr to return"
    return str([k[CONST_HRKEY] for k in heartrateDict[patient_id]])


@app.route("/api/heart_rate/average/<patient_id>", methods=["GET"])
def getAllAvg(patient_id):
    """
    look up patient and return avg of all heart rates

    :returns: string of avg heart rate
    """
    if(validatePid(patient_id, patientDict, heartrateDict) == -1):
        return "no hr to return"
    return str(numpy.average([float(k[C]) for k in heartrateDict[patient_id]]))


@app.route("/api/heart_rate/interval_average", methods=["POST"])
def getAvgSince():
    """
    Receives patient id, and datestring and returns hr since that datestring

    :returns: -1 or heart rate
    """
    r = request.get_json()
    res = intervalAvgHelper(r, patientDict, heartrateDict)
    if res == -1:
        return "Error"
    else:
        return str(res)


if __name__ == "__main__":
    """
    Runs server, intializes logging
    """
    logging.basicConfig(filename='server.log', level=logging.INFO,
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info("Starting New Log...")
    app.run(host="127.0.0.1")
