def validatePatient(input):
    """
    Validates patient dict input, checking that fields are proper and exist

    :returns: -1 if not successful, 1 if successful
    """
    if(not isinstance(input, type({}))):
        return -1
    if "patient_id" not in input.keys():
        return -1
    if "attending_email" not in input.keys():
        return -1
    if "user_age" not in input.keys():
        return -1
    try:
        if(int(input["user_age"]) < 0):
            return -1
        if(int(input["patient_id"]) < 0):
            return -1
    except:
        return -1
    return 1
