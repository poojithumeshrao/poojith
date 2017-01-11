#include<stdio.h>
void main()
{
	long int f=0,n,x=1,i,y=2,sum=0;
	while(f<4000000)
	{
		f=x+y;
		x=y;
		y=f;
		if(f%2==0)
			sum=sum+f;
	}
	printf("%ld",sum+2);
}
