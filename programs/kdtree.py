k = 3
count = 0
root = None

import numpy as np
import pdb
import graphviz as gv


class node:
    def __init__(self,k,d):
        self.points = d
        self.order = k
        self.left = None
        self.right = None

def search(nod,point):
    nn = nod
    #pdb.set_trace()
    while (True):
        if nn == None:
            print 'error'
        elif nn.points[nn.order] >= point[nn.order]:
            if nn.left == None:
                temp = nn
                lorr = 0
                break
            else :
                nn = nn.left
        else:
            if nn.right == None:
                temp = nn
                lorr = 1
                break
            else :
                nn = nn.right
    return temp,lorr

def insert(temp,lorr,point):
    #pdb.set_trace()
    t = node((temp.order+1)%k,point)
    if lorr == 0:
        temp.left = t
    else:
        temp.right = t
data = np.random.randint(low = -50,high=50,size=(10,k))

print data

g = gv.Graph(format='svg')
def plot(no):
    if no == None:
        return
    p = str(no.order)+str(no.points)
    if no.left != None:
        l = str(no.left.order)+str(no.left.points)
        g.node(l)
        g.edge(p,l,label='left')
        plot(no.left)
    if no.right != None:
        r = str(no.right.order)+str(no.right.points)
        g.node(r)
        g.edge(p,r,label='right')
        plot(no.right)
    filename = g.render(filename='img/g1')



for cord in data:
    #pdb.set_trace()
    if count == 0:
        root = node(0,cord)
    else :
        a,b = search(root,cord)
        insert(a,b,cord)
    count+=1
plot(root)


