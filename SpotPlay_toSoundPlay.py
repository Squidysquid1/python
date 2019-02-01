import time
import subprocess
#TODO: try a bunch of diffrent browesers and promt the user the preffered browser.
#TODO: add a gui with tkinter
  
def openTab(searchTerms):
  #parse search terms just enter url for now
  p = subprocess.Popen(["chrome", searchTerms])
  #TODO: check when the subprocess is killed then open new tab.
  poll = p.poll()

def checkPStatus(): #if returns None thennnnn its running <3
  if poll != None:
    #open new tab thanks
    openTab("soundcloud.com/search?q=stairway%20to%20heaven")
