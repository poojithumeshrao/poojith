#include<iostream>
#include<stdlib.h>
#include<fstream>
using namespace std;
ofstream myfile ("memory.txt",ios :: trunc);
//myfile.open("memory.txt");
int main()
{
	int i,j,k;
	int a[1000][1000],b[1000][1000],c[1000][1000];
	for(i=0;i<1000;i++)
	{
		for(j=0;j<1000;j++)
		{
			c[i][j] = 0;
			a[i][j] = rand() % 10;
			b[i][j] = rand() % 10;
			myfile<<&a[i][j]<<"\n";
			myfile<<&b[i][j]<<"\n";
			myfile<<&c[i][j]<<"\n";
		}
	}
	myfile.close();
	for(i=0;i<1000;i++)
	for(j=0;j<1000;j++)
	for(k=0;k<1000;k++)
		c[i][j] = c[i][j] + (a[i][k] * b[k][j]);
}	
