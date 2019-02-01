import time
import subprocess
#TODO: try a bunch of diffrent browesers and promt the user the preffered browser.
#TODO: add a gui with tkinter

def parseTerms(termsA):
  baseUrl="soundcloud.com/search?q=" #spaces should be replaced by"%20"
def openTab(url):
  #parse search terms just enter url for now
  p = subprocess.Popen(["chrome", url])
  #TODO: check when the subprocess is killed then open new tab.
  poll = p.poll()

def checkPStatus(): #if returns None thennnnn its running <3
  if poll != None:
    #open new tab thanks next in array pls
    openTab("www.soundcloud.com/search?q=stairway%20to%20heaven")
