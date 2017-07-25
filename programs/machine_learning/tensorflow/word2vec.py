import random
import pdb
import math
import cPickle
import numpy
import matplotlib.pyplot as plt
import copy
from collections import Counter
from nltk.stem.porter import *
import nltk
import unicodedata
import tensorflow as tf
import numpy as np

from nltk.corpus import stopwords
import nltk

stemmer = PorterStemmer()

with open('/home/poojith/poojith/programs/bbcsport/wtv') as text:
    strg = text.read().replace('\n',' ').lower()



vcbly = 500
#print strg
#unicodedata.normalize('NFKD',strg).encode('ascii','ignore')
strg = nltk.word_tokenize(strg.decode('utf-8'))

#strg = [stemmer.stem(i) for i in strg]
#print len(strg)

#strg = [x for x in strg if x not in stopwords.words('english') and not x.isdigit() and x.isalpha()]

strg = [x for x in strg if not x.isdigit() and x.isalpha()]

strg = [i.encode('ascii','ignore') for i in strg]
count = nltk.FreqDist(strg).most_common(vcbly)

cnt = [x for (x,y) in count]

dict = {cnt[i]:i for i in range(vcbly)}
for i in strg :
    if i not in dict :
        dict[i] = vcbly
#strset = set(strg)
#strset = list(strset)


#strset.sort()

#print strset
#print len(strset)
inp1 = []
op1 = []
for i in range(1,len(strg)-1,2):
    t1 = numpy.zeros(2).astype(int)
    t2 = numpy.zeros(2).astype(int)
    j=0
    for k in range(-1,2,1):
        if k !=0:
            t1[j]=dict[strg[i]]
            t2[j]=dict[strg[i+k]]
            j+=1
    inp1.extend(t1)
    op1.extend(t2)
inp1 = numpy.asarray(inp1)
op1 = numpy.asarray(op1)
op = []
inp = []
batch = 00
#pdb.set_trace()


bs = 100
es = 100
neg_sam = 30

train_in = tf.placeholder(tf.int32,shape=[bs])
train_lbl = tf.placeholder(tf.int32,shape=[bs,1])
in_test = np.random.choice(50,5,replace=False)
test_in = tf.constant(in_test,dtype=tf.int32)


embeddings = tf.Variable(tf.random_uniform([vcbly+1,es],-1,-1))
embed = tf.nn.embedding_lookup(embeddings,train_in)
w1 = tf.Variable(tf.truncated_normal([vcbly+1,es],stddev=1.0/math.sqrt(es)))
b1 = tf.Variable(tf.zeros([vcbly+1]))

loss = tf.reduce_mean(tf.nn.nce_loss(weights = w1,biases = b1,labels = train_lbl,inputs = embed,num_sampled = neg_sam,num_classes = vcbly+1))

optimizer = tf.train.AdamOptimizer(1e-4).minimize(loss)
#pdb.set_trace()
norm = tf.sqrt(tf.reduce_sum(tf.square(embeddings),1,keep_dims = True))
norm_embeddings = embeddings/norm
test_embed = tf.nn.embedding_lookup(norm_embeddings,test_in)
sim = tf.matmul(test_embed,norm_embeddings,transpose_b=True)
init=tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
#pdb.set_trace()
ct = 0
while True:
    del(inp)
    del(op)
    inp = []
    op = []
    #print len(inp1[0])
    if batch+100 < len(inp1):
        for i in range(batch,batch+100,1):
            inp.append(inp1[i])
            op.append(op1[i])
        batch += 100
    else :
        #pdb.set_trace()
        for i in range(batch,len(inp1),1):
            inp.append(inp1[i])
            op.append(op1[i])
        for j in range(0,100-len(inp1)%100,1):
            inp.append(inp1[i])
            op.append(op1[i])
        batch = 0
    inp = numpy.asarray(inp)
    op = numpy.asarray(op)
    bs = len(inp)
    #pdb.set_trace()
    feed_dict = {train_in : inp,train_lbl : op.reshape(len(op),1)}
    e=sess.run(loss,feed_dict = feed_dict)
    sess.run(optimizer,feed_dict = feed_dict)
    #------------------------
    if ct % 600 == 0:
        inp = inp.tolist()
        op = op.tolist()
        #pdb.set_trace()
        s=sim.eval(session = sess)
        for i in range(5):
            #pdb.set_trace()
            s[i][in_test[i]] = 0
            word = cnt[in_test[i]]
            nearest = np.argmax(s[i])
            if nearest != 500:
                near_word = cnt[nearest]
                print word + ' -> ' + near_word
        print batch
        print e
        print '--------'
        inp = numpy.asarray(inp)
        op = numpy.asarray(op)
    ct += 1
