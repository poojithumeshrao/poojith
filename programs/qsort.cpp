#include<iostream>
using namespace std;
# define n 5
int a[n];
void qsort(int, int);
int partition(int, int);
int main()
{
	int i;
	cout<<"enter "<<n<<" elements"<<endl;
	for(i=0;i<n;i++)
		cin>>a[i];
	qsort(0,n-1);
	cout<<"the elements in the sorted order is "<<endl;
	for(i=0;i<n;i++)
		cout<<a[i]<<"\t";
}
void qsort(int low,int high)
{
	int t;
	t=partition(low,high);
	if(low!=t-1 and t!=0)
		qsort(low,t-1);
	if(high!=t+1 and t!=high)
		qsort(t+1,high);
}
int partition(int low,int high)
{
	int temp2,pi;
	pi=a[high];
	int i=0;
	while(a[i]!=pi)
	{
		if(a[i]>pi)
		{
			temp2=a[i];
			a[i]=a[high-1];			
			a[high-1]=a[high];
			a[high]=temp2;
			high--;
		}
		if(a[i]<pi)
		i++;
	}
	return high;
}
