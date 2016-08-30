#!usr/bin/python27
import os,sys
import numpy as np 
import pandas as pd 
import csv
from difflib import SequenceMatcher
from sklearn.cluster import k_means
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


#reading files
data = pd.read_csv('ColdplaySongs.csv')
#converting lyrics of the song which is in list of sentences orginally to one single string

#lyrics = map(lambda x: ''.replace('\n',''),data['lyrics'])
lyrics = data['lyrics']
matrix = np.zeros((73,73))

for i in range(len(matrix)):
	for j in range(len(matrix)):
		matrix[i,j] = similar(lyrics[i],lyrics[j])


matrix_cluster = k_means(matrix,n_clusters = 5)
mc1 = matrix_cluster[1]
i = 0
while(i<5):
	print 'in cluster'+str(i)
	for m in range(len(mc1)):

		if mc1[m] == i:
			print data['songs'][m]

	i = i+1	



