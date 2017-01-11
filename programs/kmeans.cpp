#include<iostream>
#include<math.h>
#include<stdlib.h>

using namespace std;
struct point
{
    int x;
    int y;
}p[10];
struct cluster
{
    point val;
    cluster *next;
}*temp, *clust[3];
int d[3][10];
void add (cluster*,point);
void del (cluster*,point);
int search (point);
void assign();
void centroid();
int main()
{
	    point intial[3];
	    int low,i,j,n,m;
	
		//generate 3 clusters
		for(i=0;i<3;i++)
			{
			clust[i]=new(cluster);
			clust[i]->next=NULL;
			}
	    // Generate 10 points.
	    for(i=0;i<10;i++)
	    {
	        p[i].x=rand() % 1000;
	        p[i].y=rand() % 1000;
	    }
	    // assume 3 random centroids by pointing the first element of linked list to the centroid
       	    for(i=0;i<3;i++)
	        {
		    n=rand() % 10;	
	            clust[i]->val=p[n];
	        }
	//assigning the points to the clusters for the first time
		for(j=0;j<10;j++)
    {
        for(i=0;i<3;i++)
        {
            d[i][j]=sqrt(pow((clust[i]->val.x-p[j].x),2)+pow((clust[i]->val.y-p[j].y),2));
        }
        low = d[0][j];
        for(i=0;i<3;i++)
           { 
		if(low>d[i][j])
                {low= d[i][j];
                n=i;}
       	   }
		add(clust[n],p[j]);
    }
		centroid();
	for(i=0;i<3;i++)
	intial[i]=clust[i]->val;
	do
	{
		m=0;
		assign();
		centroid();
		for(i=0;i<3;i++)
		{
		if(clust[i]->val.x==intial[i].x && clust[i]->val.y==intial[i].y)
		m++;
		}
	}
	while(m!=3);
}
//function to add a point to the cluster
void add (cluster *first,point elem)
{
	temp=new(cluster);
	temp->val = elem;
	temp->next=first->next;
	first->next=temp;
}
//function to delete a point from the cluster
void del (cluster *first, point elem)
{
	while(first->next != NULL)
	{
		temp=first;
		temp=temp->next;
		if(temp->val.x==elem.x && temp->val.y==elem.y)
		{
			first->next= temp->next;
			delete(temp);
			break;
		}
		first=first->next;
		}
}
//function to search a point in the cluster
int search (point a)
{
	for(int i=0;i<3;i++)
	{
	while(clust[i]->next != NULL)
		{
			clust[i]=clust[i]->next;
			if(clust[i]->val.x==a.x && clust[i]->val.y==a.y)
			{ return(i);
			break;	
			}
		}
	}
}
//function to find the centroid of the cluster
void centroid()
{
for(int i=0;i<3;i++)
{
int totx=0,toty=0,n=0;
cluster *te;
te = clust[i];
	while(clust[i]->next!=NULL)
	{
		clust[i]=clust[i]->next;
		totx=totx+clust[i]->val.x;
		toty=toty+clust[i]->val.y;
		n++;
	}
if(te->next != NULL)
{
clust[i]->val.x=totx/n;
clust[i]->val.y=toty/n;
}
}
}
// Compute the distance between point and centroid and assign them to a cluster.
void assign()
{ 
int low,n,i,j,s;
   for(j=0;j<10;j++)
    {
        for(i=0;i<3;i++)
        {
            d[i][j]=sqrt(pow((clust[i]->val.x-p[j].x),2)+pow((clust[i]->val.y-p[j].y),2));
        }
        low = d[0][j];
        for(i=0;i<3;i++)
            if(low>d[i][j])
                {low= d[i][j];
                n=i;}
	s=search(p[j]);
	del(clust[s],p[j]);
        add(clust[n],p[j]);
    }
}
