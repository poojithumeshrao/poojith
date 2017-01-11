#include<iostream>
#include<stdlib.h>
using namespace std;
# define n 1
int mcoloring(int);
int nextval(int);
int g[n+1][n+1],k,i,j,x[n+1]={0};
int main()
{
	for(i=1;i<n+1;i++)
	for(j=1;j<n+1;j++)
	{
		if(i>j)
		g[i][j] = rand() % 2;
		g[j][i] = g[i][j];
	}
	for(i=1;i<n+1;i++)
	{for(j=1;j<n+1;j++)
	cout<<g[i][j]<<"\t";
	cout<<endl;}
	k=1;
	mcoloring(k);				
}
int mcoloring(int a)
{
	while(1)
	{
		nextval(a);
		if(x[a]==0)
			return 0;		
		if(a==n)
		{
			cout<<"successfully coloured with "<<m<<" colours"<<endl;
			for(i=1;i<n+1;i++)
			cout<<x[i]<<"\t";
			cout<<endl;
			return 0;
		}
		else
		{	
			a++;
			mcoloring(a);
		}	
	}
}
int nextval(int a)
{
	while(1)
	{
		x[a] = (x[a] + 1) % (m+1);
		if(x[a]==0)
			return 0;
		for(j=1;j<n+1;j++)
		{
			if(g[a][j] == 1 and x[j] == x[a] and x[j] != 0)
				break;
		}
		if(j == n+1)
			return 0;
	}
}
