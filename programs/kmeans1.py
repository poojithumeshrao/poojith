import random
import math
import pdb

#pdb.set_trace()

n = 2;

ip = 100;#number of points

#generate random points
def rndm(point): 
    point.x = random.randint(0,10);
    point.y = random.randint(0,10);

class point:
    def __init__(self):
        self.nw = 0;
        self.dis = 0;
        self.d = [];
        self.old = -1;
    def duster(self):
        for i in range(n):
            self.d.append(math.sqrt((self.x - c[i].centroid.x)**2 + (self.y-c[i].centroid.y)**2))
	self.old= self.nw
        self.nw = self.d.index(min(self.d));#new cluster
        self.dis = min(self.d);
	del self.d[:]

class cluster:
    def __init__(self):
        self.ps = []
        self.centroid = point();
        self.status = 0
        self.temp = point()
    def cal_cen(self):
        self.sumx = 0;
        self.sumy = 0;
        self.status = 0
        if(len(self.ps) != 0):
            for i in range(len(self.ps)):
                self.sumx = self.sumx + self.ps[i].x
                self.sumy = self.sumy + self.ps[i].y
            self.temp.x = self.centroid.x
            self.temp.y = self.centroid.y
            self.centroid.x = self.sumx//len(self.ps);
            self.centroid.y = self.sumy//len(self.ps);
            if self.temp.x == self.centroid.x and self.temp.y == self.centroid.y:
                self.status = 1;

#generate random points


def ch():
    for i in range(n):
        if c[i].status == 0:
            return 1
    return 0
p = []
for i in range(ip):
    p.append(point());
    
for i in range(ip):
    p[i].x = i
    p[i].y = i+1
'''p[0].x =1.0 
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
p[6].y =4.5'''
c =[cluster() for i in range(n)]
#generate random centroid
c[0].centroid.x = 0
c[0].centroid.y = 1
c[1].centroid.x = 1 
c[1].centroid.y = 2
for i in range(n):
    print str(c[i].centroid.x) +',' +str(c[i].centroid.y)

print "------------------------"

for i in range(ip):
    print str(p[i].x) +',' +str( p[i].y)
        
print "-----------------------------------------"

# implementing kmeans
count = 0
while ch():
    for point_count in range(ip):
        p[point_count].duster();
        if count != 0 :#for 1st iteration
            c[p[point_count].old].ps.remove(p[point_count]);
        c[p[point_count].nw].ps.append(p[point_count]);
    for i in range(n):
        c[i].cal_cen()
    count+=1


for i in range(n):
    print str(c[i].centroid.x) +',' +str(c[i].centroid.y)
print '--------------------'
for i in range(n):
    for j in range(len(c[i].ps)):
        print str(c[i].ps[j].x) + ',' + str(c[i].ps[j].y)
    print '-----------'
 
