#include<iostream>
#include<stdlib.h>
using namespace std;
#include "queue1.cpp"
struct job
{
	int prior;
	queue *w;
	int len;
	int time;
};
struct jobq
{
	job task;
	jobq *next;
}*start;
void enq(job);
//void deq(jobI);
void enq(job process)
{
	jobq *temp;
	temp = new(jobq);
	temp->task=process;
	temp->next=start->next;
	start->next=temp;
}
/*void deq()
{
	
	if(start->next!=NULL)
	{
		jobq *temp,*p;
		job a;												
		temp = start;
		while(temp->next!= NULL)
		{
			p =temp;
			temp=temp->next;
		}
		a=temp->task;
		delete(temp);
		p->next = NULL;
		cout<<a<<endl;
	}
}*/
int main()
{
	int n,i,count;
	job temp;
	start = new(jobq);
	cout<<"enter the number of jobs"<<endl;
	cin>>n;
	cout<<"let the priorities be 3,2,1"<<endl;
	for(i=0;i<n;i++)
	{
		temp.w = new(queue);
		//cout<<"enter the length of job\n";
		temp.len=rand()%50;
		cout<<temp.len<<endl;
		//temp.w->next=NULL;
		for(int t=0;t<temp.len;t++)
			{
				enqueue(temp.w, rand()%20);
			}
		//cout<<"enter the priority\n";
		temp.prior=rand()%4;
		temp.time=0;
		enq(temp);
	}
	int flag=1;
//checking if the process queue is empty
	while(flag==1)
	{
		jobq *temp1;
		count =0;
		temp1 = start->next;
//dequeuing without updating priorites for 4 times
		while(count<4)
		{
			temp1 = start->next;
			while(temp1 !=NULL)
			{
//checking if the priority is 3
				if(temp1->task.prior==3)
				{
//dequeuing 5 elements
					for(i=0;i<5;i++)
						//check if the job is empty
						if(temp1->task.len>0)
						{
							dequeue(temp1->task.w);
							temp1->task.len--;
							temp1->task.time++;
						}
						//if the job is empty delete the job;
						else
							temp1->task.prior=4;
				
				}
				else if(temp1->task.prior < 3)
					temp1->task.time += 5;
				temp1 = temp1->next;
			}
			count++;
		}
		temp1 = start->next;
		while(temp1!=NULL)
		{
//checking if the priority is less than 3 and updating
			if(temp1->task.prior<3)
				temp1->task.prior++;
			temp1 = temp1->next;			
		}
		temp1=start->next;
		flag=0;
		while(temp1!=NULL)
		{
			if(temp1->task.prior<4)
				{
					flag =1;
					break;
				}
			temp1 = temp1->next;	
		}
	}
//outputting the time
	jobq *temp1=start->next;
	while(temp1!=NULL)
	{
	//	if(temp1->task.prior==4)
			cout<<temp1->task.time<<endl;
			temp1 = temp1->next;			
	}
}

						

				
			
		
		
		
														
				
		
	
	

	
	
