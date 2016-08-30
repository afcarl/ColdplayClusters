import pandas as pd 
import numpy as np 
from sklearn.cluster import k_means

data = pd.read_csv("AVStream.csv")
vs = []
vsl = []

for val in data['valence stream'][:]:
	try:
		to_num = val[1:-1].split(',')
		#print vs
		vs.append(map(lambda x:float(x.replace(' ','')),to_num))
		vsl.append(len(to_num))
	except:
		print val[1:-1].split(','),'errorwa'



maxl = max(vsl)
#print maxl
ind = 0
for v in vs:
	#print v
	al = [-1]*(maxl - len(v))
	v = v + al
	vs[ind] = v
	ind += 1



# #print vs[0]
#print vs
cols = map(lambda x: 'sent1'+str(x),range(maxl))
data1 = pd.DataFrame(index=range(75),columns = cols)
data1 = data1.fillna(-1)



priya = np.array(vs)
est = k_means(priya, n_clusters = 5)[1]
print len(est)
for i in range(5):
	print '\n'
	print 'in cluster',str(i)
	print '\n'
	for k in range(len(est)):
		if est[k] == i:

			print data['songs'][k]