import subprocess
import re
import os
import spotipy
import spotipy.oauth2 as oauth2
import sys
#TODO: try a bunch of diffrent browesers and promt the user the preffered browser. and os
#TODO: add a gui with tkinter

CHROME = os.path.join('C:\\', 'Program Files (x86)', 'Google', 'Chrome', 'Application', 'chrome.exe')#for windows
token = generate_token()
spotify = spotipy.Spotify(auth=token)

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

def generate_token():
    credentials = oauth2.SpotifyClientCredentials(
        client_id="YOUR_CLIENTID",
        client_secret="YOUR_CLIENTSECRET")
    token = credentials.get_access_token()
    return token

def getSpotifySongs(username, playlist_id):
    a=[]
    token = generate_token()
    results = spotify.user_playlist(username, playlist_id, fields='tracks,next,name')
    print('Writing {0} tracks'.format(results['tracks']['total']))
    tracks = results['tracks']
    while True:
            for item in tracks['items']:
                if 'track' in item:
                    track = item['track']
                else:
                    track = item
                try:
                    track_name = track['name']+" by: "+track['artists'][0]['name']
                    a.append(track_name)
                except KeyError:
                    print("Skipping track {0} by {1} (local only?)".format(
                            track['name'], track['artists'][0]['name']))
            # 1 page = 50 results
            # check if there are more pages
            if tracks['next']:
                tracks = spotify.next(tracks)
            else:
                break
    return a


getSpotifySongs(sys.argv[1], sys.argv[2])#userid, playlist id this is for testing <3

#run this once everthing has ran its course
for x in range(0,len(testA)):
    checkPStatus(openTab(testA[x]))
