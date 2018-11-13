import logging


def validatePatient(input):
    """
    Validates patient dict input, checking that fields are proper and exist

    :returns: -1 if not successful, 1 if successful
    """
    if(not isinstance(input, type({}))):
        logging.error("didn't pass in dict")
        return -1
    if "patient_id" not in input.keys():
        logging.error("patient id missing")
        return -1
    if "attending_email" not in input.keys():
        logging.error("attending email missing")
        return -1
    if "user_age" not in input.keys():
        logging.error("user age missing")
        return -1
    try:
        if(int(input["user_age"]) < 0):
            logging.errror("user age out of bounds")
            return -1
        if(int(input["patient_id"]) < 0):
            logging.errror("patient id out of bounds")
            return -1
    except:
        logging.error("non numeric user age or patient id")
        return -1
    return 1
