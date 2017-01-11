#include "queue.cpp"
# define n 3
#include<iostream>
#include<stdlib.h>
void initialize();
void augment(char ,char);
int free(char);
char find(char);
struct label
{
	char in;
	char out;
}arr[100];
int t;
char match[]={'\0'};
using namespace std;
int main()
// set v consists of A,B,C,D......
// set u consists of a,b,c,d......
{
	t=0;
	start=new(queue);
	int i,j,g[n][n],count=0;
	for(i=1;i<n+1;i++)
	for(j=1;j<n+1;j++)
	{
		g[i][j] = rand() % 2;
	}
	initialize();
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=n;j++)
			cout<<g[i][j]<<"\t";
		cout<<endl;
	}
	while(!empty())
	{
		char w,v,u;
		w=dequeue();
		i=(int)w - 64;
		//to check if char belongs to v or u 
		if((int)w<97)
		{
			//identifing adjacent vertices
			for(j=1;j<=n;j++)
			{
				if(g[i][j]==1)
				{
					//checking if the vertex is free
					if(free((char)(j+96)))
					{
						match[i]=(char)(j+96);
						int temp1 = i+64;
						//checking if the vertex is labeled and augmenting
						while(find((char)temp1!='\0'))
						{
							u = find((char)temp1);
							match[i]='\0';
							v = find(u);
							match[(int)v-64]=u;
						}
						//remove all labels
						int g=0;
						while(arr[g].in!='\0')
						{
							arr[g].in='\0';
							arr[g].out='\0';
							g++;
						}
						while(start->next!=NULL)
							dequeue();
						initialize();
						break;
					}
					else
					{
						if((char)(j+96)!=match[i] and find((char)(j+96))=='\0')
						{
							augment(w,(char)(j+96));
							enqueue((char)(j+96));
						}
					}
				}
			}	
		}
		else
		{
			int g=0;
			while(match[g]!='\0')
			{
				g++;
				if(match[g]==(char)(i+96))
					break;
			}
			if(g!=0)
			{
				augment((char)(j+96),(char)(g+64));
				enqueue((char)(g+64));
			}
		}
		count++;
	}
	for(i=1;i<=n;i++)
	cout<<match[i]<<"\t";
	cout<<count;			
	exit(0);
}
void initialize()
{
	for(int i=65;i<65+n;i++)	
	{
		if(match[i-64]=='\0')
			enqueue((char)i);
	}
}
void augment(char f,char ne)
{
	arr[t].in=f;
	arr[t].out=ne;
	t++;
	arr[t].in='\0';
}
char find(char fi)
{
	int temp1=0;
	while(arr[temp1].in!='\0')
	{
		if(arr[temp1].in==fi)
			return arr[temp1].out;
		temp1++;
	}
	return '\0';
}
int free(char a)
{
	for( int g=1;g<=n;g++)
	{
		if(match[g]==a)
			return 0;
	}
	return 1;
}
