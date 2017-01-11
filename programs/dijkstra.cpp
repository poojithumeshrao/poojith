#include "queue.cpp"
#include<iostream>
#include<algorithm>
#include<limits>
using namespace std;
# define n 5
struct vertex
{
	int prev;
	int d;
}l[n+1],temp[n+1];
void qsort(int, int);
int partition(int, int);
int g[n+1][n+1],x[n+1][n+1],u[n+1][n+1]={0},temp_i=0;
void add_to_array(int,int);
int main()
{
	int i,j;
	int a = std::numeric_limits<int>::max();
	for(i=1;i<=n;i++)
	for(j=1;j<=n;j++)
	{
		if(i==j or i==n)
			g[i][j]=0;
		else if(g[j][i] == 0) 
		{
			g[i][j]=rand() % 5;
			g[j][i] = g[i][j];
		}
	}
	g[1][n]=0;
	start=new(queue);
	start->next=NULL;
	enqueue(1);
	l[1].prev=0;
	l[1].d=0;
	int ele,temp5,temp4=2;
	queue *p;
	p = start->next;
	while(temp5 != 0)
	{
		ele = p->ele;
		for(j=1;j<=n;j++)
		{
			if(g[ele][j]>0 and check(j))
			{
				add_to_array(g[ele][j],j);
			}
		}
		if(temp_i>1)
		{
			qsort(0,temp_i-1);
			for(i=0;i<temp_i;i++)
				enqueue(temp[i].prev);	
		}
		else if(temp_i==1)
			enqueue(temp[0].prev);
		temp_i=0;
		temp5 = count() - temp4;
		p = start->next;
		for(i=0;i<temp5;i++)
			p = p->next;
		temp4++;
	}
	for(i=2;i<=n;i++)
	{
		l[i].d = a;
		l[i].prev = 0;
	}
	l[1].d = 0;	
	int t;
	while(!empty())
	{
		ele = dequeue();
		for(j=1;j<=n;j++)
		{
			if(g[ele][j]>0 and l[ele].prev!=j)
			{
				t = l[ele].d + g[ele][j];
				if(t<l[j].d)
				{
					l[j].d = t;
					l[j].prev = ele;
				}
			}
		}
	}
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=n;j++)
			cout<<g[i][j]<<"\t";	
		cout<<endl;
	}
	for(i=1;i<=n;i++)
	{
		cout<<"distance of "<<i<<" from source is "<<l[i].d<<endl;
	}				
}
void add_to_array(int a,int b)
{
	temp[temp_i].d=a;
	temp[temp_i].prev=b;
	temp_i++;
}
void qsort(int low,int high)
{
	int t;
	t=partition(low,high);
	if(low!=t-1 and t!=0)
		qsort(low,t-1);
	if(high!=t+1 and t!=high)
		qsort(t+1,high);
}
int partition(int low,int high)
{
	int temp2,pi,temp3;
	pi=temp[high].d;
	int i=0;
	while(temp[i].d!=pi)
	{
		if(temp[i].d>pi)
		{
			temp2=temp[i].d;
			temp3=temp[i].prev;
			temp[i].d=temp[high-1].d;
			temp[i].prev=temp[high-1].prev;			
			temp[high-1].d=temp[high].d;
			temp[high-1].prev=temp[high].prev;
			temp[high].d=temp2;
			temp[high].prev=temp3;
			high--;
		}
		if(temp[i].d<pi)
		i++;
	}
	return high;
}
			
	
