#include<iostream>
# define n 2
# define m 2
using namespace std;
int comp();
float abs(float);
float tab[n+1][2*n+1]={0},array[m];
int main()
{
	int i,j,temp=0,temp1,temp2;
	float min,max,temp3;
	/*cout<<"enter number of variables"<<endl;
	cin>>n;
	cout<<"enter the number of constraints "<<endl;
	cin>>m;*/
	int obj[n+1]={0},cons[m+1][n+1],var[n+1]={0},basic[n];
	cout<<"enter the coefficients"<<endl;
	for(i=0;i<n;i++)
		cin>>obj[i];
	cout<<"enter the constraints"<<endl;
	for(i=0;i<m;i++)
	for(j=0;j<=n;j++)
		cin>>cons[i][j];
	cout<<"---"<<endl;
	//--------------------initialization
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			tab[i][j] = cons[i][j];
		}
		tab[i][n+temp]=1;
		temp++;
		tab[i][2*n] = cons[i][n];  
	}	
	for(j=0;j<n;j++)
	{
		tab[m][j] = -obj[j];
	}
	//looping starts here-----------
	//--------------------optimality test
	while(comp())
	{
	//--------finding the entering variable
	//--------finding the max of absolute vals of objective row 
		max=0;
		temp = 0;
		for(j=0;j<2*n;j++)
		{
			if(abs(tab[m][j])>max and tab[m][j]<0)
			{
				max = tab[m][j]; 
				temp = j;
			}
		}
	// -----finding the departing variable
		min = 100;
		temp2=0;
		for(i=0;i<m;i++)
		{
			if(tab[i][temp]>=0)
			{
				temp1 = (tab[i][2*n])/(tab[i][temp]);
				if(min > temp1)
				{
					min = temp1;
					temp2 = i;
				}
			}
		}
	//-----------pivoting
		temp3 = tab[temp2][temp];
		for(i=0;i<=2*n;i++)
		{
			if(temp3>0)
			tab[temp2][i] = tab[temp2][i]/temp3;
		}
		for(i=0;i<=m;i++)
		{
			if(i != temp2)
			{
				temp3 = tab[i][temp];
				for(j=0;j<=2*n;j++)	
				{
					tab[i][j] = tab[i][j] -(temp3 * tab[temp2][j]); 				
				}
			}	
		}
	}
	for(i=0;i<m;i++)
		cout<<tab[i][2*n]<<endl;	
}
int comp()
{
	for(int i=0;i<=2*n;i++)
		if(tab[m][i] < 0)
			return 1;
	return 0;
}	
float abs(float a)
{
	if(a >= 0)
		return a;
	else
		return -a;
}
