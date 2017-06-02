public class problem_21{
    public static void main(String[] args){
	int sum,temp;
	int n=10000;
	int[] num = new int[100000];
	num[1]=0;
	num[2]=1;
	int count=0;
	for(int i=3;i<=n;i++){
	    for(int j=1;j<=i/2;j++){
		if(i%j==0)
		    num[i]=num[i]+j;
	    }
	}
	for(int i=2;i<10000;i++)
	    if(num[num[i]]==i && num[i]!=i){
		System.out.println(i+ "  "+num[i] );
		count=count+num[i];
	    }
		System.out.println(count);
    }
}
		
