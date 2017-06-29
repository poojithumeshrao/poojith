import numpy
import pdb
from  scipy import misc
from PIL import Image

maskr = 5
maskc = 5

mask = numpy.ones((5,5))
#mask[0][0] = 0
#mask[4][4] = 0
#mask = numpy.array([[1,1,1],[1,1,1],[1,1,1]]) 
#pdb.set_trace()

#mask = mask/float(numpy.sum(mask))
mask = numpy.flip(numpy.flip(mask,0),1)

def getmat(a,b,mat):
    retmat = numpy.zeros((maskr,maskc))
    #pdb.set_trace()
    c = a
    d = b
    i = maskr/2
    j = maskc/2
    while c >= 0 and i >= 0:
        d=b
        j = maskc/2
        retmat[i][j] = mat[c][d]
        while d>=0 and j>=0:
            retmat[i][j] = mat[c][d]
            d-=1
            j-=1
        d = b
        j = maskc/2
        while d<len(mat[0]) and j<maskc:
            retmat[i][j] = mat[c][d]
            d+=1
            j+=1
        c -= 1
        i -= 1

    c = a
    d = b
    i = maskr/2
    j = maskc/2
    while c < len(mat) and i < maskr:
        d = b
        j = maskc/2
        retmat[i][j] = mat[c][d]
        while j<maskc and d<len(mat[0]):
            retmat[i][j] = mat[c][d]
            d+=1
            j+=1
        d=b
        j = maskc/2
        while d>=0 and j>=0:
            retmat[i][j] = mat[c][d]
            d-=1
            j-=1
        c += 1
        i += 1
    return retmat
    
inp = numpy.ones((3,3))
#op = numpy.zeros((7,7))
#print getmat(5,5,inp)
#inp = numpy.array([[2,4,6],[8,10,12],[14,16,18]])
#inp =  misc.imread('1.png')
#pdb.set_trace()
op = numpy.zeros((inp.shape))
#rop = op.astype(int)
#print inp.shape
'''
for i in range(len(inp)):
    for j in range(len(inp[i])):
        if inp[i][j]>0:
            inp[i][j] = 255
#print inp
'''
for i in range(len(inp)):
    for j in range(len(inp[i])):
        #pdb.set_trace()
        temp = getmat(i,j,inp) * mask
        #print getmat(i,j,inp)
        op[i][j] = numpy.sum(temp)
'''
for i in range(len(op)):
    for j in range(len(op[i])):
        if op[i][j]>0:
            inp[i][j] = int(255)
        else:
            inp[i][j] = int(0)
#print inp
print rop
print '-----------------'
print inp
print rop.shape
#print inp
img = Image.fromarray(inp,'L')
img.save('op.png')
img.show()
'''

print op
