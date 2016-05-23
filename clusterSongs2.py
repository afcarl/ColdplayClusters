import numpy as np 
import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
data = pd.read_csv('Coldplay Lyrics.csv')

vectorizer = CountVectorizer(min_df=1)
#print vectorizer
X = vectorizer.fit_transform(data['lyrics'])

#print X
#print vectorizer.get_feature_names()
print np.shape(X.toarray())