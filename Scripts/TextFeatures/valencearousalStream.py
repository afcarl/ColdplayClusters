import numpy as np 
import pandas as pd 
from anew_module import anew
import os,sys
from difflib import SequenceMatcher

def similar(a):

	l = []
	for a1 in a:
		for b in ['Wohoo','Oh']:

			l.append(SequenceMatcher(None, a1, b).ratio())

		#print l
	try:	
		return(max(l))	
	except: 
		return(0)	


coldplay_specs = ['Wohoo','Oh',]
data = pd.read_csv('ColdplaySongs.csv')
data['arousal stream'] = [0]*len(data)
data['valence stream'] = [0]*len(data)
songLyrics = data['lyrics'][:]
i = -1
for lyrics in songLyrics:
	#print lyrics
	i = i+1
	arousal = []
	valence = []
	lyrics = lyrics.split('\n')
	lyrics = map(lambda x:x.replace('\r',''),lyrics)
	lyrics = filter(lambda x:x!='',lyrics)
	#print lyrics
	for line in lyrics:
		#print line
		
		# print lyrics,'lyrics'

		term_list = line.split()
		#print term_list
		
		# for term_list in term_list:
		arousal.append(anew.sentiment(term_list)['arousal'])
		valence.append(anew.sentiment(term_list)['valence'])

		if (anew.sentiment(term_list)['arousal']==0 and similar(term_list)>0.7):
			arousal.pop()
			arousal.append(5)
			valence.pop()
			valence.append(6)

	#print arousal		







	#print arousal	
	data['arousal stream'][i] = str(arousal)
	data['valence stream'][i] = str(valence)
data.to_csv('AVStream.csv')

