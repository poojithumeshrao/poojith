import gzip
import cPickle
import numpy
import pdb

f = gzip.open('mnist.pkl.gz')
train_set, valid_set, test_set = cPickle.load(f)
f.close()
 
#print train_set[0][47637][323]

output = [[1,0,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0,0],[1,1,1,1,0,0,0,0,0,0],[1,1,1,1,1,0,0,0,0,0],[1,1,1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,0,0,0],[1,1,1,1,1,1,1,1,0,0],[1,1,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,1,1,1]]

f = open("opdataset.p","wb")

temp = []
#pdb.set_trace()
'''
for items in test_set[0]:
    t = []
    j = 0
    while(j <len(items)):
        for m in range(7):
            summ = [0 for co in range(7)]
            for o in range(4):
                for k in range(7):
                        #for l in range(len(items[i])):
                    summ[k] = sum(items[j:j+4]);
                    j += 4
            avg = [l/4 for l in summ]
            avg = [1 if itm>=0.2 else 0  for itm in avg] 
            t = t + avg
        temp.append(t)
                        
'''

ot = []
for items in train_set[1]:
    ot.append(output[items])


#print output[test_set[1][0]]
cPickle.dump(ot,f)
#print len(ot)
#print len(temp[47637][323])
print (ot[0])
print train_set[1][0]
f.close()
