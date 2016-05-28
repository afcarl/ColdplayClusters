import os 
import pandas as pd 

data = pd.read_csv('ColdplaySongs.csv')
f1 = data['songs']
f = os.listdir('C:\Users\priya\OneDrive\Documents\PassionProjects\ColdplayClusters\CC')
f = map(lambda x:x.replace('.wav',''),f)
f1 = map(lambda x:x.replace('.txt',''),f1)

print filter(lambda x:x not in f,f1)