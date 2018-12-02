#Title: ChatBot Dev Version
#Author: Dwight Reid
#Copyright 2018

#from basic import basic_actions

import random, datetime, calendar, os
import xml.etree.ElementTree as ET

class CB:
    def __init__(self):
        self.allCmds = []
        self.allActns = []
        self.initialiseSys()
    ################################################################################
    def getCmds(self):
        v = []
        actns = []
        for app in os.listdir('.'):
            if os.path.isdir(app):
                tree = ET.parse(app + '/commands.xml')
                cmds = tree.getroot()
                vals = []
                #v = []
                #actns = []
                cnt = 1
                for cmd in cmds:
                    for child in cmd:
                        #print child.tag, child.text
                        if child.tag == "var":
                            vals.append(child.text)
                        if child.tag == "actn":
                            actns.append(child.text)
                    v.append(vals)
                    vals = []
        return v, actns
        ################################################################################
    def redHammingMod(self,s1, s2):
        s1 = s1 + ' ' * (len(s2) - len(s1))
        s2 = s2 + ' ' * (len(s1) - len(s2))
        distance = sum(i == j for i, j in zip(s1, s2))
        norm_distance = distance / float(len(s1))
        return norm_distance
    ################################################################################
    def evaluateCommand(self,uc):
        allCmds = self.allCmds
        allActns = self.allActns
        maxX = 0
        x = 0
        cmdSel = 0

        for cnt in range(len(allCmds)):
            for cmd in allCmds[cnt]:
                x = self.redHammingMod(cmd, uc)
                if maxX < x:
                    maxX = x
                    cmdSel = cnt
    ##    print "maxX is:", maxX
    ##    print "Cmnd is:", cmdSel
    ##    print "Action ID is: ", allActns[cmdSel]

        return self.doAction(allActns[cmdSel])
    ################################################################################
    def doAction(self,actnID):
        y = actnID.split(".")
        x = __import__(y[0] + "." + y[1])
        z = y[1] + "." + y[2]
        t = getattr(x, y[1])
        u = getattr(t, y[2])
        res = u()
        del(x)
        return res
            
    ################################################################################
    def initialiseSys(self):
        #global allCmds
        #global allActns
        self.allCmds, self.allActns = self.getCmds()
        #print self.allCmds
        #print self.allActns
        #x = self.allActns[0]
        #x
        print "System Initialised"
    #timeCmds = allCmds[0]
    #dayCmds = allCmds[1]

##x = CB()
##x.initialiseSys()
##x.evaluateCommand("time")
##print "hello, welcome to my world. I am super chatbot :) "
##promptMsg = ["Enter your request ","How can I help ", "what do you want to know "]
##dispMsg = promptMsg[random.randint(1,3)-1]
##user_cmd = raw_input(dispMsg)
##evaluateCommand(user_cmd)


