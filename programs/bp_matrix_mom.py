import random
import pdb
import math
import cPickle
import numpy
import matplotlib.pyplot as plt
import copy
import collections

nip = 2
inp =[]
inp = numpy.array([[0,0],[0,1],[1,1],[1,0]])
op = numpy.array([[0],[1],[1],[1]])
b1 = 0.9
b2 = 0.999
hist1 = []
hist2 = []
counthist = 0
#fig,axes = plt.subplots(
def sigmoid(temp):
    temp = temp.tolist()
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            temp[i][j] = 1/float((1+math.exp(-temp[i][j]))) 
    return numpy.array(temp)
class hidden:
    def __init__(self,i,n,o,h):
        self.no_nodes = n
        self.no_input = i
        self.no_output = o
        self.h = numpy.zeros((h,n))
        self.ho = numpy.zeros((h,n))
        self.delta = self.ho
        self.der = self.delta
        self.inwght = numpy.random.uniform(low = -1,high = 0.5,size =(i,n))
        self.inwghttrans = self.inwght.transpose()
        self.deltatrans = self.delta.transpose()
        self.hotrans = self.ho.transpose()
        self.momentum = numpy.zeros((i,n))
        self.delin = self.momentum
        self.sumdelinsqr = self.delin
        self.v = self.momentum
layer = []
hid = [5,3]
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
create_layers(4,2,1)
#pdb.set_trace()

def backpropagation(layer,mom,lr):
    check = 1
    count = 1
    plotx = []
    ploty = []
    while check > 0.0001 :
        #----------------forwardfeed------------------
        layer[0].ho = layer[0].h = inp
	layer[0].der = layer[0].ho*(numpy.ones(layer[0].ho.shape)-layer[0].ho)
        for i in range(len(layer)-1):
            layer[i+1].h = numpy.dot(layer[i].ho,layer[i+1].inwght)
            layer[i+1].ho = sigmoid(layer[i+1].h)
            layer[i+1].der = layer[i+1].ho*(numpy.ones(layer[i+1].ho.shape)-layer[i+1].ho)
        
            #---------backwardfeed---------------
            one = numpy.ones(layer[-1].ho.shape)
            layer[-1].delta=numpy.subtract(op,layer[-1].ho)*layer[-1].ho*(numpy.subtract(one,layer[-1].ho))
            #layer[-1].delta *= 0.75
            error = numpy.square(numpy.subtract(op,layer[-1].ho))*0.5
            check = numpy.mean(error)
            for i in range(len(layer)-2,-1,-1):
                layer[i+1].deltatrans = layer[i+1].delta.transpose()
                layer[i+1].hotrans = layer[i+1].ho.transpose()
                if i!=0:
                    layer[i].delta = numpy.dot(layer[i+1].inwght,layer[i+1].deltatrans).transpose()
                    layer[i].delta *= layer[i].der
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
	pdb.set_trace()
        #print layer[-1].ho
        #print count
        '''
        if count == 0 or count %1 == 0:
            plotx.append(count)
            ploty.append(check)
        count +=1
        
    if mom:
        plt.plot(plotx,ploty,'r-',label='adam')
    else :
        plt.plot(plotx,ploty,'b-',label='sgm')
    '''
        count += 1
        if count > 10000:
            break
    if mom:
        hist1.append(count)
    else :
        hist2.append(count)
error_rate = 0
lrt = 1
while(error_rate<50):
    del hist1[:]
    del hist2[:]
    for i in range(100):
        del layer[:]
        create_layers(4,2,1)
        layer1 = copy.deepcopy(layer)
        layer2 = copy.deepcopy(layer)
        backpropagation(layer1,True,lrt)
        #pdb.set_trace()
        backpropagation(layer2,False,lrt)
        print i    
    error_rate = max(hist1.count(10001),hist2.count(10001))
    print error_rate
    print lrt
    lrt+=1
    print hist1
    print hist2
plt.hist(hist1,normed = True,bins = 30,label='adam')
plt.hist(hist2,normed = True,bins = 30,label='sgm')
plt.legend()
plt.show()
