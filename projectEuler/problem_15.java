public class problem_15{
    final int n = 3;
    long count =0;
    //  int[][] grid = new int[50][50];
    void route(int a,int b){
	System.out.println(a + "  " + b + "  " + count);
	if(b<n)
	    route(a,b+1);
	if(a<n)
	    route(a+1,b);

	if(a==n && b==n)
	    count++;
	
    }
	    
    public static void main(String[] args){
	
	problem_15 p = new problem_15();
	int i,j,k;
	p.route(0,0);
	System.out.println(p.count);
    }
}
