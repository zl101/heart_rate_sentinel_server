import logging
tachyarr = [0.006, 0.017, 0.575, 0.164, 0.44, 0.95, 3, 5, 8, 12, 16, 1000]
hrarr = [159, 166, 182, 179, 186, 169, 151, 137, 133, 130, 119, 100]


def checkTachy(age, nheartrate):
    """
    Checks if heartrate tachycardic based on hr and age

    :returns: 1 if tachycardic, -1 if not, 0 if error
    """
    try:
        numage = float(age)
        numhr = float(nheartrate)
    except:
        logging.error("unable to convert age and hr")
        return 0

    for i in range(len(tachyarr)):
        if tachyarr[i] > numage:
            if hrarr[i] < numhr:
                return 1
            else:
                return -1
    return 0
