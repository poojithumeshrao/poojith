public class problem_10{
    problem_10(){}
    boolean checkPrime(long a){
	for(int i=2;i<=a/2;i++)
	    if(a%i==0)
		return(false);
	return(true);
    }
    public static void main(String args[]){
	problem_10 p = new problem_10();
	//int set[] = new int[10];
	int set[] ={1,7,11,13,17,19,23,29};
	long sum = 2+3+5+7+11+13+17+19+23+29;
	long count=30;
	long n = 1;
	while(count<2000000){
	    for(int i=0;i<set.length;i++){
		count = (n*30) + set[i];
		if(p.checkPrime(count) && count<2000000 ){
		    System.out.println(count);
		    sum = sum + count;
		}
	    }
	    n++;
	}
	System.out.println(sum);
    }
}
	    
	
	
