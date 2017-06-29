import sklearn.datasets as dataset
import numpy
import pdb
import copy

a = dataset.load_iris()

inp = numpy.asarray(a.data)
op = numpy.asarray(a.target)


#weight = numpy.random.uniform(-0.1,0.1,size = (len(inp),1+len(inp[0])))
#delta = numpy.random.uniform(-1,1,size = (len(inp),1+len(inp[0])))
weight = numpy.zeros(1+len(inp[0]))
delta = numpy.zeros(1+len(inp[0]))
error = numpy.zeros((506,1))
gop = numpy.zeros((op.shape))


mean = inp.mean(axis=0)
inpn = (mean-inp)*(-1)
opn = (numpy.mean(op)-op)*(-1)
inp = inpn
op = opn

def linreg(lr):#inp,weight,delta,error,gop,op):
    #pdb.set_trace()
    for i in range(len(inp)):
        temp = float(weight[0])
        for j in range(len(inp[i])):
            temp+=inp[i][j]*weight[j+1]
        gop[i]=temp
        error[i] = op[i]-gop[i]
    #pdb.set_trace()
    erj = numpy.sum(error**2) /2
    for i in range(len(inp)):
        delta[0] = error[i]
        for j in range(len(inp[i])):
            delta[j+1] = error[i]*inp[i][j]
            weight[j]+=lr*delta[j]
        #weight[i]+=0.0000029787*delta[i]
    #pdb.set_trace()
    return erj

weightn = numpy.zeros((len(inp),1+len(inp[0])))
deltan = numpy.zeros((len(inp),1+len(inp[0])))
errorn = numpy.zeros((506,1))
gopn = numpy.zeros((op.shape))
count = 0
l = 0.00000000012
a=0
while count<10000:
    b=a
    a=linreg(l)
    if a<b:
        l *= 1.019
    elif a>b :
        l/=1.1
    #a = linreg(inp,weight,delta,error,gop,op)
    #an = linreg(inpn,weightn,deltan,errorn,gopn,opn)
    #print 'direct : '+ str(a) + '   normalized :  ' + str(an)
    if count%100  == 0:
        print count
        print l
        print a
        print b
    count += 1

a = numpy.ones((506,1))
b = copy.deepcopy(inp)
inpne = numpy.c_[a,b]
a = numpy.linalg.inv(numpy.dot(inpne.transpose(),inpne))
b=numpy.dot(inpne.transpose(),op)
deltane = numpy.dot(a,b)

print weight

print deltane
