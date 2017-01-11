#define n 10
#include<iostream>
using namespace std;
int main()
{
	long int i,temp,m;
	long int lcm(long int ,long int);
	temp=6;
	for(i=4;i<n;i++)
		temp=lcm(temp,i);
	cout<<temp;
}
long int lcm(long int a,long int b)
{
	long int r,t1,t2;
	r=a%b;
	t1=a;
	t2=b;
	while(r!=0)
	{
		r=a%b;
		a=b;
		b=r;
	}
	return(t1*t2/a);
}
