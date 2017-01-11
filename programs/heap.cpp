#include<iostream>
using namespace std;
void heapify_up(int[],int);
void heapify_down(int[],int);
int n=0;
int main()
{
  int h[50],val,c=0,i;
  while(c<=3)
    {
      cout<<"1 to insert"<<endl;
      cout<<"2 to minimum"<<endl;
      cout<<"3 to print heap"<<endl;
      cout<<"4 to exit"<<endl;
      cin>>c;
      switch( c)
	{
	case 1:
	  {
	    cin>>val;
	    n++;
	    h[n]=val;
	    heapify_up(h,n);
	    break;
	  }
	case 2:
	  {
	    if(n>0)
	      {
		cout<<"-------------";
		cout<<h[1]<<endl;
		h[1]=100;
		heapify_down(h,1);
		h[n]=0;
		n--;
	      }
		break;
	  }
	case 3:
	  {
	    cout<<"------------"<<endl;
	    for(i=1;i<=n;i++)
	      cout<<h[i]<<"\t";
	    cout<<endl;
	    break;
	  }
	default:
	  break;
	}
    }
}
void heapify_up(int h[],int i)
{
  int j,temp;
  if(i>1)
    {
      j=i/2;
      if(h[j]>h[i])
	{
	  temp=h[j];
	  h[j]=h[i];
	  h[i]=temp;
	  heapify_up(h,j);
	}
    }
}
void heapify_down(int h[],int i)
{
  int j,temp;
  if(2*i>n)
    return;
  else if(2*i<n)  
    {
      if(h[2*i]>h[2*i+1])
	j=2*i+1;
      else
	j=2*i;
    }
  else 
    j=2*i;
  if(h[i]>h[j])
    {
      temp=h[j];
      h[j]=h[i];
      h[i]=temp;
      heapify_down(h,j);
    }
}
