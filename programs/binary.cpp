#include<iostream>
using namespace std;
int main()
{
	int m,f,l,n,ele;
	cout<<"enter the number of elements"<<endl;
	cin>>n;
	int a[n];
	cout<<"enter the numbers"<<endl;
	for(int i=0;i<n;i++)
		cin>>a[i];
	cout<<"enter the number to be searched"<<endl;
	cin>>ele;
	f=0;
	l=n;
	do
	{
		m=(f+l)/2;
		if(a[m]==ele)
		{
			cout<<"element successfully found at "<<m+1<<endl;
			break;
		}
		if(ele>a[m])
			f=m+1;
		if(ele<a[m])
			l=m;
	}
	while(f!=l);		
}
