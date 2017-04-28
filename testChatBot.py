import random, datetime, calendar

def redHammingMod(s1, s2):
    s1 = s1 + ' ' * (len(s2) - len(s1))
    s2 = s2 + ' ' * (len(s1) - len(s2))
    distance = sum(i == j for i, j in zip(s1, s2))
    norm_distance = distance / float(len(s1))
    return norm_distance

def evaluateCommand(uc):
    maxX = 0
    x = 0
    cmdSel = 0

    for cmd in timeCmds:
       x = redHammingMod(cmd, uc)
       if maxX < x:
          maxX = x
          cmdSel = 1

    for cmd in dayCmds:
       x = redHammingMod(cmd, uc)
       if maxX < x:
          maxX = x
          cmdSel = 2

    print maxX
    print cmdSel

    if cmdSel == 1:
       print "the current time is: "
       print datetime.datetime.now().time()

    if cmdSel == 2:
       print "today is: "
       weekday = datetime.datetime.now().weekday()
       print calendar.day_name[0]

timeCmds = ["what time is it", "what is the time", "time"]
dayCmds = ["what day is it", "what day is today", "day", "what day is today", "today"]

print "hello, welcome to my world. I am super chatbot :) "
promptMsg = ["Enter your request ","How can I help ", "what do you want to know "]
dispMsg = promptMsg[random.randint(1,3)-1]
user_cmd = raw_input(dispMsg)
evaluateCommand(user_cmd)


