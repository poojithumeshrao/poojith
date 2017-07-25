import random
import pdb
import math
import cPickle
import numpy
import matplotlib.pyplot as plt
import copy
import collections
from nltk.stem.porter import *


nip = 2
inp =[]
#inp = numpy.array([[0,0],[0,1],[1,1],[1,0]])
#op = numpy.array([[0],[1],[1],[1]])
b1 = 0.9
b2 = 0.999


def sigmoid(temp):
    '''
    temp = temp.tolist()
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            temp[i][j] = 1/float((1+math.exp(-temp[i][j]))) 
    return numpy.array(temp)
    '''
    return temp
class hidden:
    def __init__(self,i,n,o,h):
        self.no_nodes = n
        self.no_input = i
        self.no_output = o
        self.h = numpy.zeros((h,n))
        self.ho = numpy.zeros((h,n))
        self.delta = self.ho
        self.der = self.delta
        self.inwght = numpy.random.uniform(low = -0.5,high = 0.5,size =(i,n))
        self.inwghttrans = self.inwght.transpose()
        self.deltatrans = self.delta.transpose()
        self.hotrans = self.ho.transpose()
        self.momentum = numpy.zeros((i,n))
        self.delin = self.momentum
        self.sumdelinsqr = self.delin
        self.v = self.momentum
layer = []
hid = [300]
def create_layers(numex,inp,out):
    global hid
    layer.append(hidden(0,inp,hid[0],numex))
    if len(hid) != 1:
        for i in range(len(hid)):
            h = hid
            if i == 0:
                layer.append(hidden(layer[0].no_nodes,h[i],h[i+1],numex))
                continue
            elif i == len(hid)-1:
                layer.append(hidden(h[i-1],h[i],out,numex))
                continue
            else : # i!=0 and i!=len(hid) :
                layer.append(hidden(h[i-1],h[i],h[i+1],numex))
    else :
        layer.append(hidden(inp,hid[0],out,numex))
    layer.append(hidden(layer[-1].no_nodes,out,0,numex))
#pdb.set_trace()

def backpropagation(mom,lr):
    check = 1
    count = 1
    plotx = []
    ploty = []
    while count < 2:
        #----------------forwardfeed------------------
        layer[0].ho = layer[0].h = inp
	#layer[0].der = layer[0].ho*(numpy.ones(layer[0].ho.shape)-layer[0].ho)
        for i in range(len(layer)-1):
            layer[i+1].h = numpy.dot(layer[i].ho,layer[i+1].inwght)
            layer[i+1].ho = sigmoid(layer[i+1].h)
            #layer[i+1].der = layer[i+1].ho*(numpy.ones(layer[i+1].ho.shape)-layer[i+1].ho)
            layer[-1].ho = numpy.exp(layer[-1].h - numpy.max(layer[-1].h))
            layer[-1].ho /= layer[-1].ho.sum()
                                
            #---------backwardfeed---------------
            one = numpy.ones(layer[-1].ho.shape)
            layer[-1].delta=numpy.subtract(op,layer[-1].ho)*layer[-1].ho*(numpy.subtract(one,layer[-1].ho))
            #layer[-1].delta = numpy.subtract(op,layer[-1].ho)
            #layer[-1].delta *= 0.75
            error = numpy.square(numpy.subtract(op,layer[-1].ho))*0.5
            check = numpy.mean(error)
            #pdb.set_trace()
            for i in range(len(layer)-2,-1,-1):
                layer[i+1].deltatrans = layer[i+1].delta.transpose()
                layer[i+1].hotrans = layer[i+1].ho.transpose()
                if i!=0:
                    layer[i].delta = numpy.dot(layer[i+1].inwght,layer[i+1].deltatrans).transpose()
                    #layer[i].delta *= layer[i].der
                layer[i+1].delin = numpy.dot(layer[i].ho.transpose(),layer[i+1].delta)
                if mom :
                    #pdb.set_trace()
                    layer[i+1].momentum = b1*layer[i+1].momentum + layer[i+1].delin * (1-b1)
                    layer[i+1].sumdelinsqr+= numpy.square(layer[i+1].delin)
                    layer[i+1].v = b2 * layer[i+1].v + (1-b2)*numpy.square(layer[i+1].delin)
                    m1 = layer[i+1].momentum / (1-b1**count)
                    v1 = layer[i+1].v / (1-b2**count)
                    adam = 0.001*(m1/(numpy.sqrt(v1) + 0.000000001))
                    layer[i+1].inwght += lr*adam
                else :
                    layer[i+1].inwght += lr*(layer[i+1].delin + layer[i+1].momentum)
                #print check
        count += 1    
    return check

from nltk.corpus import stopwords
import nltk

with open('/home/poojith/poojith/programs/bbcsport/wtv') as text:
    strg = text.read().replace('\n',' ').lower()

#print strg


strg = nltk.word_tokenize(strg.decode('utf-8'))

print len(strg)

strg = [x for x in strg if x not in stopwords.words('english') and not x.isdigit() and x.isalpha()]



strset = set(strg)
strset = list(strset)


strset.sort()

#print strset
print len(strset)
create_layers(100,len(strset),len(strset))
inp1 = []
op1 = []
for i in range(2,len(strg)-2,1):
    t1 = numpy.zeros((4,len(strset)))
    t2 = numpy.zeros((4,len(strset)))
    for j in range(4):
        t1[j][strset.index(strg[i])] = 1
        for k in range(-2,2,1):
            if k !=0:
                t2[j][strset.index(strg[i+k])] = 1
    inp1.extend(t1)
    op1.extend(t2)
inp1 = numpy.asarray(inp1)
op1 = numpy.asarray(op1)
op = []
batch = 00
#pdb.set_trace()
ct = 0
while True:
    del(inp)
    del(op)
    inp = []
    op = []
    #print len(inp1[0])
    if batch+100 < len(inp1[0]):
        for i in range(batch,batch+100,1):
            inp.append(inp1[i])
            op.append(op1[i])
        batch += 100
    else :
        #pdb.set_trace()
        for i in range(batch,len(inp1[0]),1):
            inp.append(inp1[i])
            op.append(op1[i])
        for j in range(i,batch+99,1):
            inp.append(inp1[i])
            op.append(op1[i])
        batch = 0
    inp = numpy.asarray(inp)
    op = numpy.asarray(op)
    e = backpropagation(False,1)
    if ct % 22 == 0:
        inp = inp.tolist()
        op = op.tolist()
        ho = layer[-1].ho[10].tolist()
        #pdb.set_trace()
        print batch
        print e
        print strset[inp[10].index(1)]
        print strset[op[10].index(1)]
        #print max(ho)
        print strset[ho.index(max(ho))]
        print '--------'
        inp = numpy.asarray(inp)
        op = numpy.asarray(op)
    ct += 1
