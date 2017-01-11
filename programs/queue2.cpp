#include<iostream>
using namespace std;
struct queue
{
	group *ele;
	queue *next;
}*start;
void enqueue(int);
int dequeue();
int empty();
int check(int);
int count();
int  dequeue()
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
void enqueue(int val)
{
	queue *temp;
	temp = new(queue);
	temp->ele=val;
	temp->next=start->next;
	start->next=temp;
}
int empty()
{
	if(start->next==NULL)
		return 1;
	else
		return 0;
}
int check(int a)
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
