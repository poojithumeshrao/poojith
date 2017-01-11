#include<iostream>
using namespace std;
struct queue
{
	int ele;
	queue *next;
}*start1,*start2;
void enqueue(queue,int);
int dequeue(queue);
int empty(queue);
int  dequeue(queue *start)
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
void enqueue(queue *start, int val)
{
	queue *temp;
	temp = new(queue);
	temp->ele=val;
	temp->next=start->next;
	start->next=temp;
}
int empty(queue *start)
{
	if(start->next==NULL)
		return 1;
	else
		return 0;
}

