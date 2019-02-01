import time
import subprocess
import re
#TODO: try a bunch of diffrent browesers and promt the user the preffered browser.
#TODO: add a gui with tkinter

def parseTerms(termsA):
  baseUrl="soundcloud.com/search?q=" #spaces should be replaced by"%20"
  parsedURL = baseURL + re.sub(' ','%20',termsA)#replacing spaces with 20%
  return parsedURL

def openTab(url):
  #parse search terms just enter url for now
  p = subprocess.Popen(["chrome", url])
  #TODO: check when the subprocess is killed then open new tab.
  
def checkPStatus(): #if returns None thennnnn its running <3
  poll = p.poll()
  if poll != None:
    #open new tab thanks next in array pls
    openTab("www.soundcloud.com/search?q=stairway%20to%20heaven")
def getJSON(url):
  jsonurl = urlopen(url)
  txt = json.loads(jsonurl.read())
  return txt
