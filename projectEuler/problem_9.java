public class problem_9{
    problem_9(){
    }
    public static void main(String args[]){
	for(int a=100;a<=600;a++)
	    for(int b=100;b<=600;b++)
		{
		    if((1000000 + 2*a*b - 2*(a+b)*1000)==0)
			System.out.println(a*b*(1000-a-b));
		}
    }
}

