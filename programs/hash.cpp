#include "ll.cpp"
#include<iostream>
using namespace std;
# define n 5
int main()
{
	char a[];
	int i;
	ll *hash[n];
	for(i=0;i<n;i++)
	{
		hash[i] = new(ll);
		hash[i]->next = NULL;
	}
	while(1)
	{	
		cin>>a;
		i=0;
		while(1)
		{
			if(a[i] == '\0')
				break;
		}
		add(a,hash[i%n]);
		if(a == '\0')
			break;
	}	
}
