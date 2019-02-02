import time
import subprocess
import re
import os
import json
#TODO: try a bunch of diffrent browesers and promt the user the preffered browser. and os
#TODO: add a gui with tkinter
testA =["www.google.com","www.minecraft.net"]

CHROME = os.path.join('C:\\', 'Program Files (x86)', 'Google', 'Chrome', 'Application', 'chrome.exe')


def parseTerms(termsA):
  baseUrl="soundcloud.com/search?q=" #spaces should be replaced by"%20"
  parsedURL = baseURL + re.sub(' ','%20',termsA)#replacing spaces with 20%
  return parsedURL

def openTab(url):
  #parse search terms just enter url for now
  p = subprocess.Popen([CHROME, url])
  return p
  
def checkPStatus(process): #if returns None thennnnn its running <3
    poll = None
    while poll == None:
        poll = process.poll()


def getJSON(url):
  jsonurl = urlopen(url)
  txt = json.loads(jsonurl.read())
  return txt



#run this once everthing has ran its course
for x in range(0,len(testA)):
    checkPStatus(openTab(testA[x]))

