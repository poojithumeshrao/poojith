public class problem_6{
    public static void main(String args[]){
	int a=99;
	int sum = a+1,tot = 0;
	while(a!=0){
	    tot = tot +(a*sum);
	    sum = sum + a;
	    a--;
	}
	System.out.println(2*tot);
    }
}
	
