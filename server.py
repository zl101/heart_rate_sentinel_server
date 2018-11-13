from flask import Flask, jsonify, request
import requests
from valpatient import validatePatient
app = Flask(__name__)
patientDict = {}
heartrateDict = {}
CONST_PIDKEY = "patient_id"
CONST_EMAILKEY = "attending_email"
CONST_AGEKEY = "user_age"


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
    return "Patient Added"

if __name__ == "__main__":
    app.run(host="127.0.0.1")
