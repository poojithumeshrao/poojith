#include<iostream>
#include<stdlib.h>
using namespace std;
# define n 8
int x[n+1],count=0;
int place(int,int);
void nqueens(int);
int main()
{
	for(int i=1;i<n+1;i++)
	x[i]=-1;
	int k=1;
	nqueens(k);
	cout<<count<<" number of solutions";
}
int place(int k, int i)
{
	int j;
	for(j=1;j<k;j++)
	{
		if(x[j]==i or abs(x[j]-i)==abs(j-k))
		return 0;
	}
	return 1;
}
void nqueens(int k)
{
	for(int j=1;j<n+1;j++)
	{
		if(place(k,j))
		{
			x[k]=j;
			if(k==n)
			{
				for(int z=1;z<n+1;z++)
				cout<<x[z]<<"\t";
				cout<<endl;
				count++;
			}
			else
			nqueens(k+1);
		}
	}
}
