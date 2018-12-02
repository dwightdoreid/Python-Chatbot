import random, datetime, calendar

################################################################################
def getTime():
##    print "the current time is: "
##    print datetime.datetime.now().time()
    return datetime.datetime.now().time()
################################################################################
def getDay():
##    print "Today is: "
##    weekday = datetime.datetime.now().weekday()
##    print calendar.day_name[0]
    return calendar.day_name[0]
################################################################################
def getIP():
    print "I don't know what it is"

################################################################################
