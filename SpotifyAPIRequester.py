import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import numpy as np
import pandas as pd



#access api creds
credentials = json.load(open('C:/Users/dorothy/source/repos/SpotifyAnalysis/SpotifyAPICreds.json'))
client_id = credentials['client_id']
client_secret = credentials['client_secret']
client_credentials_manager = SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#fetch audio features
features = sp.audio_features('574y1r7o2tRA009FW0LE7v')
features_df = pd.DataFrame(data=features, columns=features[0].keys())

#collecting data for an artist's tracks
tracks = (sp.search(q='artist:'  + 'Ed Sheeran', type='track'))

#cleaning up data
data = json.dumps(tracks)
data = json.loads(data)
data = data['tracks']
stringtracks = str(tracks)
stringtracks = stringtracks.replace("'", '"')
stringtracks = stringtracks.replace("False", '"False"')
stringtracks = stringtracks.replace("None", '"None"')

#filtering data for only audio features
jsonobject = json.loads(stringtracks)
tracks = jsonobject["tracks"]
items = tracks["items"]

#creating list to collect audio features for each track
trackId = []

for item in items:
    trackId.append(item["id"])

audiofeatures = sp.audio_features (tracks = trackId)
print (audiofeatures)
   
for id in trackId:
    print(id)
