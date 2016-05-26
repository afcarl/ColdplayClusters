#!/usr/bin/python27
# -*- coding: <utf8> -*-

import gensim
import nltk
import re
import string
import pandas as pd
import numpy as np

data = pd.read_csv("ColdplaySongs.csv")
doc = data['lyrics']

punc = re.compile( '[%s]' % re.escape( string.punctuation ) )
term_vec = [ ]
for d in doc:
  d = d.lower()
  d = punc.sub( '', d )
  term_vec.append( map(lambda x:unicode(x,errors='ignore'),nltk.word_tokenize( d ) )) # Print resulting term vectors

#for vec in term_vec: 
#  print vec

# Remove stop words from term vectors

stop_words = nltk.corpus.stopwords.words( 'english' )

for i in range( 0, len( term_vec ) ):
    term_list = [ ]

    for term in term_vec[ i ]:
        if term not in stop_words:
            term_list.append( term )

    term_vec[ i ] = term_list

# Print term vectors with stop words removed

#for vec in term_vec:
#    print vec

#  Convert term vectors into gensim dictionary
print term_vec
dict = gensim.corpora.Dictionary(term_vec)
corp = [ ]
for i in range( 0, len( term_vec ) ):
    corp.append( dict.doc2bow( term_vec[ i ] ) )

#  Create TFIDF vectors based on term vectors bag-of-word corpora
tfidf_model = gensim.models.TfidfModel( corp )

tfidf = [ ]
for i in range( 0, len( corp ) ):
    tfidf.append( tfidf_model[ corp[ i ] ] )

#  Create pairwise document similarity index

n = len( dict )
index = gensim.similarities.SparseMatrixSimilarity( tfidf_model[ corp ], num_features = n )

#  Print TFIDF vectors and pairwise similarity per document

for i in range( 0, len( tfidf ) ):
    s = 'Doc ' + str( i + 1 ) + ' TFIDF:'

    for j in range( 0, len( tfidf[ i ] ) ):
        s = s + ' (' + dict.get( tfidf[ i ][ j ][ 0 ] ) + ','
        s = s + ( '%.3f' % tfidf[ i ][ j ][ 1 ] ) + ')'

    print s

for i in range( 0, len( corp ) ):
    print 'Doc', ( i + 1 ), 'sim: [ ',

    sim = index[ tfidf_model[ corp[ i ] ] ]
    for j in range( 0, len( sim ) ):
        print '%.3f ' % sim[ j ],

    print ']'
