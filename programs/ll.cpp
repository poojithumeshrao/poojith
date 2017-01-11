#include<iostream>
using namespace std;
struct ll
{
	group *ele;
	queue *next;
};
void add(char,ll *);
int dequeue();
int empty();
int check(char,ll *);
int count();
int  del()
{
	if(start->next!=NULL)
	{
		queue *temp,*p;
		int a;
		temp = start;
		while(temp->next!= NULL)
		{
			p =temp;
			temp=temp->next;
		}
		a=temp->ele;
		delete(temp);
		p->next = NULL;
		return(a);
	}
	
}
group* add(char val,ll *start)
{
	ll *temp;
	temp = new(ll);
	temp->next=start->next;
	start->next=temp;
	temp->ele = val; 
	return temp;
}
int empty()
{
	if(start->next==NULL)
		return 1;
	else
		return 0;
}
int check(int a,ll *start)
{
	queue *temp;
	temp = start;
	while(temp != NULL)
	{
		if(temp->ele == a)
			return 0;
		temp = temp->next;
	}
	return 1;
}
int count()
{
	int countt=0;
	queue *temp;
	temp = start->next;
	while(temp!=NULL)
	{
		temp=temp->next;
		countt++;
	}
	return countt;
}
