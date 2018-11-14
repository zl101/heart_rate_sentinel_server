import logging


def validatePid(pid, patientDict, hrDict):
    """
    Validates patient id input for checking tachycardic

    :returns: -1 if not successful, 1 if successful
    """
    if(not isinstance(pid, type(""))):
        logging.error("didn't pass in string")
        return -1
    if pid not in patientDict.keys():
        logging.error("patient not initialized")
        return -1
    if pid not in hrDict.keys():
        logging.error("This should never happen")
        return -1
    if(len(hrDict[pid]) == 0):
        logging.error("No Heart Rate Data Available")
        return -1
    return 1
