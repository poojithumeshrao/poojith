#include<iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;
class group
{
	public:
	int a;
	group()
	{
		a=1;
	}
	int val;
	group *next;	
};
int insert(group* , int);
group* intersection(group*,group*);
group* unionn(group* , group*);
group* check(group*,int);
void print(group*);
int sparse()
{
	int n,e,ele,ar;
	cout<<"enter the number of sets"<<endl;
	cin>>n;
	group *point[n+1],*out;
	for(int i=0;i<=n;i++)
		{
			point[i] = new(group);
			point[i]->next = NULL;
		}
	while(1)
	{
		cout<<"enter 1 for inserting values into a set"<<endl;
		cout<<"enter 2 for intersection"<<endl;
		cout<<"enter 3 for union"<<endl;
		cin>>e;
		switch(e)
		{
			case 1:
			{
				cout<<"enter the set and the val"<<endl;
				cin>>ar>>ele;
				insert(point[ar],ele);
				break;
			}
			case 2:
			{
				cout<<"enter the 2 sets"<<endl;
				cin>>ar>>ele;
				print(intersection(point[ar],point[ele]));
				break;
			}
			case 3:
			{
				cout<<"enter the 2 sets"<<endl;
				cin>>ar>>ele;
				print(unionn(point[ar],point[ele]));
				break;
			}
			case 4:
			{
				cout<<"enter the set to print"<<endl;
				cin>>ele;
				print(point[ele]);
				break;
			}
			default :
				exit(0);
		}
	}
}
int insert(group *arr, int ele)
{
	group *temp;
	int i,j;
	j = ele % 32;
	if(arr->next == NULL)
	{
		temp = new(group);
		arr->next = temp;
		temp->val = ele/32;
		for(i=0;i<j;i++)
			temp->a = temp->a << 1;
		temp->next = NULL;
		return 0;
	}
	else
	{
		arr = arr->next;
		while(arr != NULL)
		{		
			if(arr->val == ele/32)
			{	
				int a = 1;
				for(i=0;i<j;i++)
				{	
					a = a << 1;
				}
				arr->a = arr->a | a;
				return 0;
			}
			if(arr->next==NULL)
				temp = arr;
			arr = arr->next;
		}
		arr = temp;
		temp = new(group);
		arr->next = temp;
		temp->val = ele/32;
		for(int i=0;i<j;i++)
			temp->a = temp->a << 1;
		temp->next = NULL;
		return 0;
	}
}	
group* unionn(group *arr, group *b)
{
	group *temp1,*temp2,*start1;
	temp1 = new(group);
	start1 = temp1;
	arr= arr->next;
	b= b->next;
	while(arr != NULL)
	{
		temp2 = new(group);
		temp2->a = arr->a;
		temp2->val = arr->val;
		temp1->next = temp2;
		temp1 = temp1->next;
		arr= arr->next;
	}
	while(b !=NULL)
	{
		if(check(start1,b->val) != NULL)
		{
			temp2 = check(start1,b->val);
			temp2->a = temp2->a | b->a;
		}
		else
		{
			temp2 = new(group);
			temp2->a = b->a;
			temp2->val = b->val;
			temp1->next = temp2;
			temp1 = temp1->next;
		}
		b=b->next;
	}
	return start1;
} 
group* intersection(group *arr, group *b)
{
	group *start1,*temp1,*temp2,*temp3;
	temp1 = new(group);
	start1 = temp1;
	arr = arr->next;
	while(arr != NULL)
	{
		if(check(b,arr->val) != NULL)
		{
			temp3 = check(b,arr->val);
			int a=1;
			temp2 = new(group);
			temp2->val = arr->val;
			temp2->a = (arr->a & temp3->a);
			temp1->next=temp2;
		}
		arr = arr->next;
	}
	return start1;
}

group* check(group *arr,int b)
{
	arr = arr->next;
	while(arr != NULL)
	{
		if(arr->val == b)
			return arr;
		arr=arr->next;
	}
	return NULL;
}									
void print(group *arr)
{
	cout<<"---"<<endl;
	int temp;
	arr = arr->next;
	while(arr!=NULL)
	{
		int a=1;
		for(int i=0;i<32;i++)
		{
			if((a & arr->a) != 0)
			{
				temp = (arr->val * 32) + i ;
				cout<<temp<<"\t";
			}
			a = a << 1;
		}
		arr = arr->next;
	}
	cout<<endl;
}
