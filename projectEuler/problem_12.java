public class problem_12{
    int factorCount(long a){
	int count=0;
	int i=1;
	for(i=1;i<a/i;i++)
	    if(a%i==0)
		count+=2;
	if(a%i==0 && a/i == i)
		count++;
	return count;
    }
    public static void main(String args[]){
	long sum = 1;
	long cur=2;
	problem_12 p = new problem_12();
	while(true){
	    sum=sum+cur;
	    //System.out.println(p.factorCount(9));
	    if(p.factorCount(sum)>=500){
		System.out.println(sum);
		break;
	    }
	    cur++;
	}
    }
}
	    
