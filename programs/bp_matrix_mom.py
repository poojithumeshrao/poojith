import random
import pdb
import math
import cPickle
import numpy
import matplotlib.pyplot as plt
import copy

nip = 2
inp =[]
inp = numpy.array([[0,0],[0,1],[1,1],[1,0]])
op = numpy.array([[0],[1],[0],[1]]) 
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

def backpropagation(layer,mom):
    check = 1
    count = 0
    plotx = []
    ploty = []
    global plt
    while check > 0.0001:
        #----------------forwardfeed------------------
        layer[0].ho = layer[0].h = inp
        for i in range(len(layer)-1):
            layer[i+1].h = numpy.dot(layer[i].ho,layer[i+1].inwght)
            layer[i+1].ho = sigmoid(layer[i+1].h)
            layer[i+1].der = layer[i+1].ho*(numpy.ones(layer[i+1].ho.shape)-layer[i+1].ho)
        
            #---------backwardfeed---------------
            one = numpy.ones(layer[-1].ho.shape)
            layer[-1].delta=numpy.subtract(op,layer[-1].ho)*layer[-1].ho*(numpy.subtract(one,layer[-1].ho))
            layer[-1].delta *= 0.75
            error = numpy.square(numpy.subtract(op,layer[-1].ho))*0.5
            check = numpy.mean(error)
            for i in range(len(layer)-2,-1,-1):
                layer[i+1].deltatrans = layer[i+1].delta.transpose()
                layer[i+1].hotrans = layer[i+1].ho.transpose()
                if i!=0:
                    layer[i].delta = numpy.dot(layer[i+1].inwght,layer[i+1].deltatrans).transpose()
                    layer[i].delta *= layer[i].der * 0.75
                layer[i+1].delin = numpy.dot(layer[i].ho.transpose(),layer[i+1].delta)
                layer[i+1].inwght += layer[i+1].delin + layer[i+1].momentum
                if mom :
                    layer[i+1].momentum = layer[i+1].delin * 1
        #print layer[-1].ho
        #print count
        if count == 0 or count %100 == 0:
            plotx.append(count)
            ploty.append(check)
        count +=1
    plt.plot(plotx,ploty)

layer1 = copy.deepcopy(layer)
layer2 = copy.deepcopy(layer)
backpropagation(layer1,True)
#pdb.set_trace()
backpropagation(layer2,False)
plt.show()
