import random
import math
import pdb

#pdb.set_trace()

n = 2;

ip = 7;#number of points

#generate random points
def rndm(point): 
    point.x = random.randint(0,10);
    point.y = random.randint(0,10);

class point:
    def __init__(self):
        self.nw = 0;
        self.dis = 0;
        self.d = []
        self.old = -1;
    def duster(self):
        for i in range(n):
            self.d.append(math.sqrt((self.x - c[i].centroid.x)**2 + (self.y-c[i].centroid.y)**2))
        self.old = self.nw
        self.nw = self.d.index(min(self.d));#new cluster
        self.dis = min(self.d);
        del self.d[:]

class cluster:
    def __init__(self):
        self.ps = []
        self.centroid = point();
    def cal_cen(self):
        self.sumx = 0;
        self.sumy = 0;
        if(len(self.ps) != 0):
            for i in range(len(self.ps)):
                self.sumx = self.sumx + self.ps[i].x
                self.sumy = self.sumy + self.ps[i].y
                self.centroid.x = self.sumx/len(self.ps);
                self.centroid.y = self.sumy/len(self.ps);

#generate random points

p = []
for i in range(ip):
    p.append(point());
    
p[0].x =1.0 
p[0].y =1.0
p[1].x =1.5
p[1].y =2.0
p[2].x =3.0
p[2].y =4.0
p[3].x =5.0
p[3].y =7.0
p[4].x =3.5
p[4].y =5.0
p[5].x =4.5
p[5].y =5.0
p[6].x =3.5
p[6].y =4.5
c =[cluster() for i in range(n)]
#generate random centroid
c[0].centroid.x = 1.0
c[0].centroid.y = 1.0
c[1].centroid.x = 5.0 
c[1].centroid.y = 7.0
for i in range(n):
    print str(c[i].centroid.x) +',' +str(c[i].centroid.y)

print "------------------------"

for i in range(ip):
    print str(p[i].x) +',' +str( p[i].y)
        
print "-----------------------------------------"

# implementing kmeans
for count in range(2):
    for point_count in range(ip):
        p[point_count].duster();
        if count != 0 :#for 1st iteration
            c[p[point_count].old].ps.remove(p[point_count]);
            c[p[point_count].old].cal_cen();
        c[p[point_count].nw].ps.append(p[point_count]);
        c[p[point_count].nw].cal_cen();
        


for i in range(n):
    print str(c[i].centroid.x) +',' +str(c[i].centroid.y)
