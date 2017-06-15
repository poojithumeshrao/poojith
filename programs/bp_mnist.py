import random
import pdb
import math
import cPickle

nip = 49
mnisti = cPickle.load(open("dataset.p","rb"))
mnisto = cPickle.load(open("opdataset.p","rb"))
mnistti = cPickle.load(open("intestset.p","rb"))
mnistto = cPickle.load(open("optestset.p","rb"))
inp =[]
inptest = []
#inp = [[0,0,0],[0,1,1],[1,1,1],[1,0,1]]
batch = 100
batchtest = 10000
for i in range(batch):
    inp.append(mnisti[i] + mnisto[i])
for i in range(batchtest):
    inptest.append(mnistti[i] + mnistto[i])

print "sucessfully loaded the mnist dataset....."

#print len(inp)
#print len(inp[0])
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
layer.append(hidden(0,49,50))
layer.append(hidden(49,50,10))
#layer.append(hidden(20,20,20))
#layer.append(hidden(20,20,20))
#layer.append(hidden(20,20,10))
layer.append(hidden(50,10,0))


count = 0
ercheck = 1

#pdb.set_trace()
while True:
    errortest = [0 for i in range(len(inptest))]
    
    batch = 100
    for i in range(batch):
        inp.append(mnisti[i] + mnisto[i])
    error = [0 for i in range(len(inp))]
    while batch <50000:
        for i in range(len(inp)): #looping through each input
#----------------------- forward feed --------------------
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
            #if count % 1 == 0:
            #print layer[1].ho
            #print str(inp[i][2]) +'  ' +  str(layer[-1].ho[0]) + ' '# + str(layer[-1].delin) + str(layer[-1].inwght)
            #----------------------- backward feed ---------------------        
            er = [0 for j in range(layer[-1].no_nodes)]
            for j in range(layer[-1].no_nodes):
                er[j]=0.5*((inp[i][j+nip]-layer[-1].ho[j])**2)
            error[i] = sum(er)
            #if batch == 100 and i == 0:
            #    pdb.set_trace()
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
            for j in range(len(layer)-1):
                for k in range(len(layer[j+1].inwght)):
                    layer[j+1].inwght[k] += layer[j+1].delin[k]
        ercheck = max(error)
        if batch != 50000:
            batch += 100
        else :
            batch = 100
        del(inp)
        inp = []
        #del(er)
        #del(error)
        for mb in range((batch-100),batch,1):
            inp.append(mnisti[mb] + mnisto[mb])
        '''
        if batchtest != 10000:
        batchtest += 100
        else :
        batchtest = 100
        del(inptest)
        
        inptest = []
        for mb in range((batchtest-100),batchtest,1):
        inptest.append(mnistti[mb] + mnistto[mb])
'''
    oprob = []
    corprob = 0
    #----------------test set----------------------------------------------------------------------------------
    for i in range(len(inptest)): #looping through each input
        #----------------------- forward feed --------------------
        #pdb.set_trace()
        for j in range(nip):#feed the current input to the first layer
            layer[0].h[j] = inptest[i][j]
            layer[0].ho[j] = inptest[i][j]
        for j in range(len(layer)-1):#looping through each layer
            for k in range(layer[j+1].no_nodes):#calculate output of each layer
                t=layer[j+1].bias
                for l in range(layer[j+1].no_input):#select hidden layer
                    t = t +(layer[j].ho[l]) * (layer[j+1].inwght[(k*layer[j+1].no_input)+l])
                layer[j+1].h[k] = t
                layer[j+1].ho[k] = sigmoid(t)
        optest = [1 if x>0.5 else 0 for x in layer[-1].ho]
        opsum = sum(optest)-1
        mnistopsum = sum(inptest[i][nip:]) - 1
        if opsum == mnistopsum:
            corprob += 1
            #if count % 1 == 0:
            #print layer[1].ho
            #print str(inp[i][2]) +'  ' +  str(layer[-1].ho[0]) + ' '# + str(layer[-1].delin) + str(layer[-1].inwght)
            #----------------------- backward feed ---------------------        
            #pdb.set_trace()
        ertest = [0 for j in range(layer[-1].no_nodes)]
        for j in range(layer[-1].no_nodes):
            ertest[j]=0.5*((inptest[i][j+nip]-layer[-1].ho[j])**2)
        errortest[i] = sum(ertest)
    #del(errortest)
    #del(ertest)
    if count % 1 == 0:
        #ercheck = 0
        print count
        print 'train error : ' + str(sum(er)/len(er)) + ' test error : ' + str(sum(ertest)/len(ertest))
        print corprob/10000.0
        print '-----------'
        
    
    count +=1;
'''
    if count % 20 == 0:
        for j in range(nip):#feed the current input to the first layer
            layer[0].h[j] = inptest[0][j]
            layer[0].ho[j] = inptest[0][j]
            for j in range(len(layer)-1):#looping through each layer
                for k in range(layer[j+1].no_nodes):#calculate output of each layer
                    t=layer[j+1].bias
                    for l in range(layer[j+1].no_input):#select hidden layer
                        t = t +(layer[j].ho[l]) * (layer[j+1].inwght[(k*layer[j+1].no_input)+l])
                        layer[j+1].h[k] = t
                        layer[j+1].ho[k] = sigmoid(t)
'''
# print layer[-1].ho
# print'---------'         
#print str(count) + ' iterations to learn'

