#include<stdio.h>
int main()
{
	long long int n=600851475143,i,j;
	for(i=n;i>0;i-=2)
		if(i%3!=0 && ((i+1)%6==0 || (i-1)%6==0))
			for(j=2;j<=i;j++);
				printf("%lld\n",i);
}
	
