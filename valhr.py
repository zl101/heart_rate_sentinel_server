import logging


def validateHeartRate(input, patientDict):
    """
    Validates patient hr input, checking that fields are proper and exist

    :returns: -1 if not successful, 1 if successful
    """
    if(not isinstance(input, type({}))):
        logging.error("input not type dict")
        return -1
    if "patient_id" not in input.keys():
        logging.error("missing patient id")
        return -1
    if "heart_rate" not in input.keys():
        logging.error("missing heart rate")
        return -1
    if input["patient_id"] not in patientDict.keys():
        logging.error("patient not initialized")
        return -1
    try:
        if(float(input["heart_rate"]) < 0):
            logging.error("invalid hr")
            return -1
    except:
        logging.error("non numeric hr")
        return -1
    return 1
