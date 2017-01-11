#include "queue.cpp" 
#include<iostream>
#include<algorithm>
using namespace std;
# define n 6
# define m 5
struct label
{
	int prev;
	int r;
	int d;
}l[n+1];
void shortestaugmentingpath();
void initialize();
int min(int,int);
int g[n+1][n+1],x[n+1][n+1]={0},u[n+1][n+1],res[n+1][n+1];
int main()
{
	int i,j;
	for(i=1;i<=n;i++)
	for(j=1;j<=n;j++)
	{
		if(j==1 or i==j or i==n)
			g[i][j]=0;
		else if(g[j][i] == 0) 
			g[i][j]=rand() % 2;
	}
	g[1][n]=0;
	for(i=1;i<=n;i++)
	{
		l[i].prev = 0;
		l[i].r=0;
	}
	for(i=1;i<=n;i++)
	for(j=1;j<=n;j++)
	{
		if(g[i][j]==1)
		{
			u[i][j]=1 + rand() % m;
		}
	}
	start = new(queue);
	start->next = NULL;
	enqueue(1);
	cout<<"the network"<<endl;
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=n;j++)
			cout<<g[i][j]<<"\t";	
		cout<<endl;
	}
	cout<<"the maximum capacity"<<endl;
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=n;j++)
			cout<<u[i][j]<<"\t";	
		cout<<endl;
	}
	initialize();
	shortestaugmentingpath();
					
}
void shortestaugmentingpath()
{
	while(!empty())
	{
		int ele;
		ele = dequeue();
		// for every edge of ele checking forward edges
		for(int j=1;j<=n;j++)
			if(g[ele][j]==1)	
			//checking if it is unlabelled
				if(l[j].prev==0)
				{
					res[ele][j]=u[ele][j]-x[ele][j];
					if(res[ele][j]>0)
					{
						l[j].r = min(l[ele].r,res[ele][j]);
						l[j].prev = ele;
						l[j].d = 1;
						enqueue(j);
					}
				}
		// for every edge of ele checking backward edges
		for(int j=1;j<=n;j++)	
			if(g[j][ele]==1)	
			//checking if it is unlabelled
				if(l[j].prev==0)
					if(x[j][ele]>0)
					{
						l[j].r = min(l[ele].r,x[j][ele]);
						l[j].prev = ele;
						l[j].d = 0;
						enqueue(j);
					}
		
		// checking if sink is labelled			
		if(l[n].prev!=0)
		{
		// augmenting path found
			int j;
			j=n;
			while(j!=1)
			{
				if(l[j].d==1)
					x[l[j].prev][j] += l[n].r;
				else
					x[l[j].prev][j] -= l[n].r;
				j = l[j].prev;
			}
			for(int i=1;i<=n;i++)
			for(j=2;j<=n;j++)
				if(i<j)
					x[j][i]=x[i][j];
			initialize();
			while(start->next != NULL)
				dequeue();
			enqueue(1);
		}
	}
	cout<<"the maximum flow path is "<<endl;
	for(int i=1;i<=n;i++)
	{	
		for(int j=1;j<=n;j++)
			cout<<x[i][j]<<"\t";
		cout<<endl;
	}

								
}
void initialize()
{
	int i;
	for(i=1;i<=n;i++)
	{
		l[i].prev = 0;
		l[i].r=0;
	}
	l[1].prev=-1;
	l[1].r=m+1;
	l[1].d=0;
}
int min(int a,int b)
{
	if(a>b)
		return b;
	else
		return a;
}
