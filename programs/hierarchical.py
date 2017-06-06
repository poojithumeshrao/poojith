import pdb
import math
import random
import scipy.spatial
#pdb.set_trace

n = 6

def minimum(list):
    if len(list)!=0 :
        m=1000000
        for i in range(len(list)):
            if(list[i]!=0 and list[i]<m) :
                m=list[i]
    return m


class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    


class cluster:
    def __init__(self):
        self.centroid = point(0,0)
        self.ps = []
    def cal_cen(self):
        self.sumx = 0;
        self.sumy = 0;
       
        if(len(self.ps) != 0):
            for i in range(len(self.ps)):
                self.sumx = self.sumx + self.ps[i].x
                self.sumy = self.sumy + self.ps[i].y
            self.centroid.x = self.sumx/len(self.ps);
            self.centroid.y = self.sumy/len(self.ps);
        

#genererate points

p = []
p.append(point(0.40,0.53))
p.append(point(0.22,0.38))
p.append(point(0.35,0.32))
p.append(point(0.26,0.19))
p.append(point(0.08,0.41))
p.append(point(0.45,0.30))

#print points
for i in range(6):
    print str(p[i].x) + ',' + str(p[i].y)
print '--------------------'


    
t1 = []
for i in range(n):
    t2 = cluster()
    t2.ps.append(p[i])
    t2.centroid.x = t2.ps[0].x
    t2.centroid.y = t2.ps[0].y
    t1.append(t2)

# implement hierarchical
c = []
c.append(t1)

count = 0

#pdb.set_trace()
while True :
    m = []
    po = [[c[count][j].centroid.x,c[count][j].centroid.y] for j in range(len(c[count]))];
    a = scipy.spatial.distance.cdist(po,po).tolist()
    for i in range(len(a)):
        m.append(minimum(a[i]))
    for i in range(len(m)):
        mi = min(m)
    x = 0
    y = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if(a[i][j]==mi):
                x=i
                y=j
                break

    nc=cluster()
    for items in c[count][x].ps:
        nc.ps.append(items)
    for items in c[count][y].ps:
        nc.ps.append(items)
    nc.cal_cen()
    nl = []
    for i in range(len(c[count])):
        if i != x :
            if i!= y:
                nl.append(c[count][i])
    nl.append(nc)
    c.append(nl)
    count += 1
    print len(c[count])
    if len(c[count]) == 1:
        break



for i in range(len(c)):
    for j in range(len(c[i])):
        for k in range(len(c[i][j].ps)):
            print str(c[i][j].ps[k].x)+","+str(c[i][j].ps[k].y)
        print "####################"
    print "____________________________"




























































#print c[0][0].ps[0].x


