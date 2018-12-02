import ChatBot as cb
import random

import SocketServer
import SimpleHTTPServer
import re

PORT = 9090

y = cb.CB()

##x = y.evaluateCommand("day")
##
##print x
def mainz():
    promptMsg = ["Enter your request ","How can I help ", "what do you want to know "]
    dispMsg = promptMsg[random.randint(1,3)-1]
    user_cmd = raw_input(dispMsg)
    print y.evaluateCommand(user_cmd)

print "hello, welcome to my world. I am super chatbot :) "

##while 1:
##    mainz()

class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        if None != re.search('/chat/*', self.path):
            cmd = str(self.path.split('/')[-1])
            cmd = cmd.strip()
            cmd = cmd.replace("%20", " ")
            cmd = cmd.replace("%22", "")
            print cmd
            print self.path.split('/')
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(y.evaluateCommand(cmd)) #call sample function here
            return
        else:
            #serve files, and directory listings by following self.path from
            #current working directory
            SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

httpd = SocketServer.ThreadingTCPServer(('', PORT),CustomHandler)

print "serving at port", PORT
httpd.serve_forever()
