from anew_module import anew
import os
import pandas as pd 
import numpy as np 
from sklearn import preprocessing
from sklearn.cluster import k_means

data = pd.read_csv('ColdplayLyrics.csv')

## GETTING THE VALENCE AND AROUSAL VALUES - PUTTING THEM IN THE withSentimenT.csv 
arousal = []
valence = []
for lyrics in data['lyrics'] :
	term_list = lyrics.split()
	#print term_list
	#print anew.sentiment(term_list)['arousal']
	arousal.append(anew.sentiment(term_list)['arousal'])
	valence.append(anew.sentiment(term_list)['valence'])

data1 = data
data1['valence'] = valence

data1['arousal'] = arousal	
train = data1[['arousal','valence']]

matrix = preprocessing.scale(train)

matrix_cluster = k_means(matrix,n_clusters = 10)
mc1 = matrix_cluster[1]
i = 0
while(i<10):
	print '\n'
	print 'in cluster'+str(i)
	print '\n'
	for m in range(len(mc1)):

		if mc1[m] == i:
			print data['songs'][m]

	i = i+1	

#data1.to_csv('withSentiment.csv')
