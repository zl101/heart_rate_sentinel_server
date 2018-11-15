import logging
import datetime
import numpy


def intervalAvgHelper(input, patientDict, hrDict):
    """
    Validates input and then returns average hr since a datetime

    :returns: -1 if not successful, otherwise the average hr
    """
    if(not isinstance(input, type({}))):
        logging.error("didn't pass in dict")
        return -1
    if "patient_id" not in input.keys():
        logging.error("patient id missing")
        return -1
    if "heart_rate_average_since" not in input.keys():
        logging.error("datetime missing")
        return -1
    if input["patient_id"] not in patientDict.keys():
        logging.error("patient not found")
        return -1
    if input["patient_id"] not in hrDict.keys():
        logging.error("should never happen")
        return -1
    if(len(hrDict[input["patient_id"]]) == 0):
        logging.error("No Heart Rate Data Available")
        return -1
    hrList = hrDict[input["patient_id"]]
    try:
        dateobj = datetime.datetime.strptime(input["heart_rate_average_since"],
                                             "%Y-%m-%d %H:%M:%S.%f")
    except:
        logging.error("could not parse date string")
        return -1
    if(dateobj > hrList[-1]["datetime"]):
        logging.error("No heart rate data in range")
        return -1
    index = 0
    for item in hrList:
        if dateobj < item["datetime"]:
            nlist = hrList[index:]
            return numpy.average([float(k["heart_rate"]) for k in nlist])
        index = index + 1
    return -1
