import os,sys
import string
import re
from pydub import AudioSegment
import numpy as np 
import pandas as pd 

path = "C:\Users\priya\OneDrive\Documents\PassionProjects\ColdplayData\ColdplaySongs/"
filenames = os.listdir(path)
f = []
for i in filenames:
	new_string = i
	for i in ['Coldplay','-',' ','lyrics','Lyrics','video','audio','Video','official','Official','.mp3',r'\(',r'\)']:
		new_string = re.sub(i,'',new_string,re.IGNORECASE)

	f.append(new_string.replace(' ',''))
	
print f


for i in range(len(filenames)):
	sound = AudioSegment.from_mp3(path+filenames[i])
	sound.export("C:\Users\priya\OneDrive\Documents\PassionProjects\ColdplayData\CC/"+filenames[i], format="wav")

# import subprocess

# subprocess.call(['ffmpeg', '-i', 'C:\Users\priya\OneDrive\Documents\PassionProjects\ColdplayClusters\ColdplaySongs\A Message (Coldplay- X&Y).mp3',
#                    'C:\Users\priya\OneDrive\Documents\PassionProjects\ColdplayClusters\Message.wav'])