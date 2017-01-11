#include<stdio.h>
int main()
{
	long long int num,i,max=1,j,m;
	printf("number\n");
	scanf("%lld",&num);
	//if((num/2) % 2 == 0)
	//	m=num/2 - 1;
	//else
	//	m
	for(i=2;i<num;i++)
	{

		if(num%i==0)
		{
			m=num/i;
			if(m%2!=0 && m%3!=0 && ((m+1)%6==0 || (m-1)%6==0))
			for(j=2;j<=m;j++)
				if(m%j==0)
					break;
			if(j==m)
			{
				max=m;	
				break;
			}
		}
	}
	printf("%lld",max);
}
