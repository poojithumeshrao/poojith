#include<iostream>
using namespace std;
# define n 5
int a[n][n];
int main()
{
  int i,j;
  void out(int);
  for(i=0;i<n;i++)
    {
      for(j=0;j<n;j++)
	{
	  a[i][j]=n*i+j+1;
	  cout<<a[i][j]<<"\t";
	}
      cout<<endl;
    }
   for(i=0;i<n/2+1;i++)
     out(i);
}
void out(int t)
{
  int i;
  for(i=t;i<n-(t);i++)
    cout<<a[t][i]<<endl;
  for(i=t+1;i<n-(t+1);i++)
    cout<<a[i][n-(t+1)]<<endl;
  for(i=n-(t+1);i>t;i--)
    cout<<a[n-(t+1)][i]<<endl;
  for(i=n-(t+1);i>=t+1;i--)
    cout<<a[i][t]<<endl;
}  
