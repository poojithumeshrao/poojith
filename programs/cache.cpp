#include<iostream>
#include<math.h>
using namespace std;
#define n 8
#define s 4
#define l 2
#define w 4
int out(int,int);
class lines
{
	public:
		int a[w];
		/*for(i=0;i<w;i++)
			a[i]=i;*/
		int tag;
		int valid;
		lines()
		{
			valid = 0;
		}	
};
struct set
{

	lines line[l];
}set[s];
int main()
{
	long long int mem,bit_offset,set_bit,temp,set_no,tag,val;
	while(1)
	{
		cin>>hex>>mem;
		/*if(mem == 0)
		{
			cout<<"zzz\n";
			break;
		}*/
		bit_offset = log2(w);
		set_bit = log2(s) + bit_offset; 
		int a=1;
		for(int i = 0;i<bit_offset;i++)
			a=a<<1;
		set_no = 0;
		for(int i=bit_offset;i<set_bit;i++)
		{
			if((a & mem) > 0)
			set_no = set_no + pow(2,i-bit_offset);
			a=a<<1;
		}
		tag=0;
		a=1;
		for(int i = 0;i<set_bit;i++)
			a=a<<1;
		for(int i=set_bit;i<n;i++)
		{
			if((a & mem) > 0)
			tag = tag + pow(2,i-set_bit);
			a=a<<1;
		}
		out(tag,set_no);
	}	
}	
int out(int tag,int set_no)
{
	for(int i=0;i<l;i++)
	{
		if(set[set_no].line[i].valid == 1 and set[set_no].line[i].tag==tag)
		{
			cout<<"cache hit\n";
			return 1;
		} 
	}
	cout<<"cache miss\n";
	if(l != 1)
	{
		for(int i=l-1;i>0;i--)
		{
			set[set_no].line[i].tag = set[set_no].line[i-1].tag;
			set[set_no].line[i].valid = set[set_no].line[i-1].valid; 
		}
	}
	set[set_no].line[0].tag = tag;
	set[set_no].line[0].valid = 1;
	return 0;
}
