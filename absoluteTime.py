import time
import datetime

#Translates current dateTime into a single integer
def absoluteTime():
    now = datetime.datetime.now()

    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    seconds = now.second
    millis = now.microsecond

    #Store total number of seconds
    yearConversion = 365 * 24 * 60 * 60 * year
    monthConversion = 30 * 24 * 60 * 60 * month
    dayConversion = 24 * 60 * 60 * day
    hourConversion = 60 * 60 * hour
    minuteConversion = 60 * minute

    timeVariable = yearConversion + monthConversion + dayConversion + hourConversion + minuteConversion

    return timeVariable
