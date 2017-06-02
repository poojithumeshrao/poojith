import random
import math
import pdb

#pdb.set_trace()

n = input("enter number of groups\n");

ip = 5;#number of points

#generate random points
def rndm(point): 
    point.x = random.randint(0,10);
    point.y = random.randint(0,10);

class point:
    def __init__(self):
        self.nw = 0;
        self.dis = 0;
        self.old = -1;
    def dist_frm_cluster(self):
        for i in range(n):
            d[i] = sqrt((x - c[i].centroid.x)**2 + (y-c[i].centroid.y)**2)
        self.nw = d.index(min(d));#new cluster
        self.dis = min(d);

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
    rndm(p[i]);

c =[cluster() for i in range(n)]
#generate random centroid
for i in range(n):
    c[i].centroid.x = p[random.randint(0,ip-1)].x
    c[i].centroid.y = p[random.randint(0,ip-1)].y

for i in range(n):
    print str(c[i].centroid.x) +',' +str(c[i].centroid.y)

print "------------------------"

for i in range(ip):
    print str(p[i].x) +',' +str( p[i].y)
        
print "-----------------------------------------"

# implementing kmeans
for count in range(5):
    for point_count in range(ip):
        p[point_count].dist_frm_cluster;
        if point_count != 0 and p[point_count].old != -1:#for 1st iteration
            c[p[point_count].old].ps.remove(p[point_count]);
            c[p[point_count].old].cal_cen();
        c[p[point_count].nw].ps.append(p[point_count]);
        c[p[point_count].nw].cal_cen();
        


for i in range(n):
    print str(c[i].centroid.x) +',' +str(c[i].centroid.y)

