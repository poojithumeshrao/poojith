import random
import pdb
import math

nip = 2
inp = [[0,0,1],[0,1,1],[1,1,1],[1,0,0]]

def sigmoid(temp):
    #print temp
    return 1/float((1+math.exp(-temp)))
class hidden:
    def __init__(self,i,n,o):
        self.no_nodes = n
        self.no_input = i
        self.no_output = o
        self.h = [0 for a in range(n)]
        self.ho = [0 for a in range(n)]
        self.inwght = [(random.uniform(-0.5,0.5)) for a in range(n*i)]
        self.bias = 1
        self.delin = [0 for a in range(n*i)]
        self.deror = [0 for a in range(n)]

layer = []
layer.append(hidden(0,2,3))
layer.append(hidden(2,3,1))
layer.append(hidden(3,1,0))

layer[0].h = [0 for i in range(2)]
layer[0].h = [0 for i in range(2)]
#layer[2].inwght = [0.3,0.2]
#layer[1].inwght = [0.1,0.2,0.3,0.4]
error = [0 for i in range(len(inp))]
count = 0
ercheck = 1
#pdb.set_trace()
while ercheck >  0.001:
    for i in range(len(inp)): #looping through each input
#----------------------- forward feed --------------------
       
        #pdb.set_trace()
        for j in range(nip):#feed the current input to the first layer
            layer[0].h[j] = inp[i][j]
            layer[0].ho[j] = inp[i][j]
        for j in range(len(layer)-1):#looping through each layer
            for k in range(layer[j+1].no_nodes):#calculate output of each layer
                t=layer[j+1].bias
                for l in range(layer[j+1].no_input):#select hidden layer
                    t = t +(layer[j].ho[l]) * (layer[j+1].inwght[(k*layer[j+1].no_input)+l])
                layer[j+1].h[k] = t
                layer[j+1].ho[k] = sigmoid(t)
        if count % 1000 == 0:
            #print layer[1].ho
            print str(inp[i][2]) +'  ' +  str(layer[-1].ho[0]) + ' '# + str(layer[-1].delin) + str(layer[-1].inwght)
            #----------------------- backward feed ---------------------        
        #pdb.set_trace()
        er = [0 for j in range(layer[-1].no_nodes)]
        for j in range(layer[-1].no_nodes):
            er[j]=0.5*((inp[i][j+nip]-layer[-1].ho[j])**2)
        error[i] = sum(er)
        for j in range(layer[-1].no_nodes):
            temp = layer[-1].ho[j]
            temp1 = (inp[i][j+nip]-temp)*temp*(1-temp)
            layer[-1].deror[j] = temp1
        
        k = 0
        for l in range(layer[-1].no_nodes):
            for m in range(layer[-1].no_input):
                layer[-1].delin[k] = layer[-1].deror[l] * layer[-2].ho[m] * (1) * 0.5
                k = k+1
        for j in range((len(layer)-2),0,-1):
            for k in range(layer[j].no_nodes):
                temp = 0
                op = layer[j].ho[k]
                for l in range(layer[j+1].no_nodes):
                    temp += layer[j+1].inwght[k*layer[j+1].no_nodes + l]*layer[j+1].deror[l]
                layer[j].deror[k] = temp*op*(1-op)
            k = 0
            for l in range(layer[j].no_nodes):
                for m in range(layer[j].no_input):
                    #pdb.set_trace()
                    layer[j].delin[k] = layer[j].deror[l] * layer[j-1].ho[m] * (1) * 0.5
                    k = k+1
        #pdb.set_trace()
        for j in range(len(layer)-1):
            for k in range(len(layer[j+1].inwght)):
                layer[j+1].inwght[k] += layer[j+1].delin[k]
    
    ercheck = max(error)
   
    if count % 1000 == 0:
        #ercheck = 0
        print count
        print ercheck
        print '-----------'
    count +=1;
print'---------'         
print str(count) + ' iterations to learn'
