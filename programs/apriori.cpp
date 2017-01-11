#include "sparse.cpp"
#include<iostream>
#include<stdlib.h>
using namespace std;
#define trans 5
#define items 10
#define minsup 5
struct ll
{
	group *set;
	int supp;
	ll *next;
}*start;
void frequent();
int support(group*);
group* check_whole_set(group *);
int del(ll*);
group* add();
void add(group*);
group *cust[trans];
int main()
{
	int i,j,k;
	for(j=0;j<trans;j++)
	for(i=0;i<(1 + rand() % items);i++)
		insert(cust[j],1+rand()%items);
	k= 1;
	for(i=0;i<items;i++)
	{
		group *temp;
		temp = add();
		insert(temp,i+1);
	}
	for(i=0;i<trans;i++)
		print(cust[i]);
	//while(start->next != NULL)
		frequent(); 
	
}
int support(group *arr)
{
	int i,j,k=0;
	arr = arr->next;
	for(j=0;j<trans;j++)
	{
		//traverse each transaction
		//traversing the given set
		while(arr != NULL)
		{
			if(arr->val == cust[j]->val)
			{
				int a=1;
				//finding the elements in the given set
				for(i=0;i<32;i++)
				{
					if((arr->a & a) != 0)
					{
						if((cust[j]->a & a) == 0)
							break;
					}
				}
				if(i == 32)
					k++;
			}
			arr = arr->next;
		}
	}
	return k;
}
void frequent()
{
	ll *temp,*temp1,*temp2;
	temp = start->next;
	while(temp!=NULL)
	{
		if(support(temp->set) < minsup)
		{
			del(temp);
			temp=temp->next;
		}
	}
	temp = start->next;
	temp1 = temp->next;
	while(temp!=NULL)
	{
		while(temp1!=NULL)
		{
			temp2->set = unionn(temp->set,temp1->set);
			if(check_whole_set(temp2->set) == NULL)
			{
				add(temp2->set);
			}
			temp1 = temp1->next;
		}
		temp1 = temp->next;
		start->next=temp->next;
		delete(temp);
		temp = temp1;
		if(temp != NULL)
			temp1 = temp->next;
	}
}
group* check_whole_set(group *b)
{
	ll *arr,*temp1;
	arr = start;
	arr= arr->next;
	b=b->next;
	group *temp;
	temp = b;
	temp1 = arr;
	while(arr != NULL)
	{
		arr->set = arr->set->next;
		while(arr->set != NULL)
		{
			while(b != NULL)
			{
				if(arr->set->val == b->val)		
					if(arr->set->a != b->a)
						break;
				b=b->next;
			}
			if(b != NULL)
				break;
			b = temp;
			arr->set = arr->set->next;
		}
		if(arr->set != NULL)
			return temp1->set; 
		arr =arr->next;
		temp1 = arr;
	}
	return NULL;
}
int  del(ll *temp3)
{
	ll *temp1,*temp2,*temp;
	temp = temp3;
	temp1 = start;
	while(temp1->next!=NULL)
	{
		temp2=temp1;
		temp1= temp1->next;
		while(temp != NULL)
		{
			if(temp1->set->val == temp->set->val and temp1->set->a == temp->set->a)
			{
			
			}
			temp = temp->next;
		}
	}
	
}
group* add()
{
	ll *temp;
	temp = new(ll);
	temp->next=start->next;
	start->next=temp;
	return temp->set;
}				
void add(group *a)
{
	ll *temp;
	temp = new(ll);
	temp->next=start->next;
	start->next=temp;
	temp->set = a;	
}
