import os
import numpy as np 
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
albums_path = "C:\Users\priya\OneDrive\Documents\Coldplay\Albums/"
albums = os.listdir(albums_path)
#You have songs from 7 albums
#['AHeadFullOfDreams', 'ARushOfBloodToTheHead', 'GhostStories', 'MyloXyloto', 'Parachutes', 'VivaLaVida', 'X&Y']
#In Total there are 73 songs
songLyrics = pd.DataFrame(columns = ['songs','lyrics'], index = range(73))
songLyrics = songLyrics.fillna(0)
t = 0
songsL = []
for album in albums:
	#go into each album
	print album
	path = albums_path+'/'+album + "/"
	# grab each each song
	for i in os.listdir(path):
		#store the lyrics and song
		print t
		print i
		with open(path+i) as songs:
			songLyrics['songs'].iloc[t] = i
			songLyrics['lyrics'].iloc[t] = songs.readlines()
		t += 1	
print songLyrics.head()
songLyrics.to_csv('Coldplay Lyrics.csv')