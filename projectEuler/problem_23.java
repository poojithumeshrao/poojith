public class problem_23{
    public static void main(String[] args){
	int sum,temp;
	int n=30000;
	int[] num = new int[100000];
	int[] t = new int[100000];
	num[1]=0;
	num[2]=1;
	sum=0;
	int count=0;
	for(int i=3;i<=n;i++){
	    for(int j=1;j<=i/2;j++){
		if(i%j==0)
		    num[i]=num[i]+j;
	    }
	}
	for(int i=2;i<30000;i++)
	    if( num[i]>i){
		//System.out.println(i+ "  "+num[i] );
		t[i]=1;
		count=count+num[i];
	    }
	
		System.out.println(num[12]);
    }
}
