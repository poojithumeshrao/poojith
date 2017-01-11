#include<iostream>
#include<math.h>
#include<stdlib.h>
#define con 10
#define num 3
using namespace std;
struct point
{
	float x;
	float y;
	int z;	
}p[con],centroid[num],initial[num];
void add(int , int);
void assign(int);
void calc_centroid();
int main()
{
	int i,j;
	//pick random points.
	for(i=0;i<con;i++)
	{
		p[i].x=rand() % 1000;
        	p[i].y=rand() % 1000;
	}
	//assume 3 random centroids.
	for(i=0;i<num;i++)
	{
		j=rand() % con;
		centroid[i] = p[j];
		centroid[i].z=i;
	}
	//to store the intial position of the centroids and check
	do	
	{
		for(i=0;i<num;i++)
		{
		initial[i]=centroid[i];
		}
		for(i=0;i<con;i++)
			assign(i);
		calc_centroid();
		j=0;
		for(i=0;i<num;i++)
		{
			if(initial[i].x==centroid[i].x && initial[i].y==centroid[i].y)
			j++;	
		}
	}
	while(j!=num);	
for(i=0;i<num;i++)
		{
			cout<<"The points in the cluster "<<i+1<<" are "<<endl;
			cout<<"Centroid "<<centroid[i].x<<"\t"<<centroid[i].y<<endl;
			for(j=0;j<con;j++)
			{	
				if(p[j].z==i)
				cout<<"point "<<p[j].x<<"\t"<<p[j].y<<endl;
			}
		}
}
//function to add the points to the cluster
void add(int c,int a)
{
	p[a].z=centroid[c].z;
}
void assign(int a)
{
	int d[num],low,temp1,temp2,i,z;
	for(i=0;i<num;i++)
	{
		temp1=pow((centroid[i].x-p[a].x),2);
		temp2=pow((centroid[i].y-p[a].y),2);
		d[i]=sqrt(temp1+temp2);
	}
	low = d[0];
	z=0;
	for(i=0;i<num;i++)
	{
		if(low>d[i])
		{
			z=i;
		}
	}
	add(z,a);
}
//function to calculate the centroid
void calc_centroid()
{
	for(int i=0;i<num;i++)
	{
		int totx=0,toty=0,n=0;
		for(int j=0;j<con;j++)
		{
			if(centroid[i].z==p[j].z)
			{
				totx=totx + p[j].x;
				toty=toty + p[j].y;
				n++;
			}
		}
		if(n!=0)
		{
			centroid[i].x = totx/n;
			centroid[i].y = toty/n;
		}
	}
}	

