#include<iostream>
#include<math.h>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
int main()
{
	long int i,j,k=0,m,temp,r=0,lar=0;;
	for(i=999;i>=990;i--)
	{
//i=993;
		for(j=i;j>=100;j--)
		{
/*j=913;*/		
			temp=m=i*j;

			while(m>=10)
				m=m/10;
			if(m==temp%10)
			{
				m=temp;
				r=0;
				while(m!=0)
				{
					r=r*10+(m%10);
					m/=10;
				}
				if(r==temp and r>lar)
				{
					lar=r;
					cout<<r<<"\t";	
				}
			}
		}
	}
	//cout<<lar;
}		
