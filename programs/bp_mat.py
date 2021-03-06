import random
import pdb
import math
import cPickle
import numpy
import matplotlib.pyplot as plt

'''nip = 2
inp =[]
inp = numpy.array([[0,0],[0,1],[1,1],[1,0]])
op = numpy.array([[0],[0],[1],[0]])
'''

nip = 49
mnisti = cPickle.load(open("dataset.p","rb"))
mnisto = cPickle.load(open("opdataset.p","rb"))
mnistti = cPickle.load(open("intestset.p","rb"))
mnistto = cPickle.load(open("optestset.p","rb"))
inp =[]
op = []
inptest = []
#inp = [[0,0,0],[0,1,1],[1,1,1],[1,0,1]]
batch = 100
batchtest = 10000
for i in range(batch):
    inp.append(mnisti[i])
    op.append(mnisto[i])
#for i in range(batchtest):
 #   inptest.append(mnistti[i])
  #  optest.append(mnistto[i])

print "sucessfully loaded the mnist dataset....."



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
hid = [100]
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
create_layers(100,49,10)
#pdb.set_trace()
check = 1
count = 0
plotx = []
ploty = []
ct =1
while True:
    while batch != 50000:
        #----------------forwardfeed------------------
        layer[0].ho = layer[0].h = inp
        for i in range(len(layer)-1):
            layer[i+1].h = numpy.dot(layer[i].ho,layer[i+1].inwght)
            layer[i+1].ho = sigmoid(layer[i+1].h)
            layer[i+1].der = layer[i+1].ho*(numpy.ones(layer[i+1].ho.shape)-layer[i+1].ho)

        #---------backwardfeed---------------
        one = numpy.ones(layer[-1].ho.shape)
        #print layer[-1].ho
        #pdb.set_trace()
        layer[-1].delta=numpy.subtract(op,layer[-1].ho)*layer[-1].ho*(numpy.subtract(one,layer[-1].ho))
        #layer[-1].ho = numpy.exp(layer[-1].h)
        #summ = layer[-1].ho.sum(axis=0)
        #layer[-1].ho /= summ[:,None]
        #print layer[-1].ho
        #layer[-1].delta=numpy.subtract(op,layer[-1].ho)
        layer[-1].delta *= 0.75
        error = numpy.square(numpy.subtract(op,layer[-1].ho))*0.5
        check = numpy.mean(error)
        #pdb.set_trace()
        for i in range(len(layer)-2,-1,-1):
            layer[i+1].deltatrans = layer[i+1].delta.transpose()
            layer[i+1].hotrans = layer[i+1].ho.transpose()
            if i!=0:
                layer[i].delta = numpy.dot(layer[i+1].inwght,layer[i+1].deltatrans).transpose()
                layer[i].delta *= layer[i].der * 0.75
                layer[i+1].delin = numpy.dot(layer[i].ho.transpose(),layer[i+1].delta)
                layer[i+1].inwght += layer[i+1].delin + layer[i+1].momentum
                layer[i+1].momentum = layer[i+1].delin * 0.5
                #print layer[i+1].delta
                #pdb.set_trace()
        #print layer[-1].ho
        print count
        print check
        #if count == 0 or count %100 == 0:
            #plotx.append(count)
            #ploty.append(check)
        count +=1
        if batch != 50000:
            batch += 100
        else :
            batch = 100
        del(inp)
        del(op)
        inp = []
        op=[]
            #del(er)
            #del(error)
        for mb in range((batch-100),batch,1):
            inp.append(mnisti[mb])
            op.append(mnisto[mb])
    pdb.set_trace()
    batch = 100
    print '----------------'
    print ct
    ct+=1
    
#plt.plot(plotx,ploty)
#plt.show()
