import java.util.Scanner;
public class problem_13{
    public static void main(String args[]){
	Scanner userInput = new Scanner(System.in);
	long[][] input=new long[100][5];
	long[] sum = {0,0,0,0,0,0};
	long a = 10000000000L;
	for(int i=0;i<100;i++)
	    for(int j=0;j<5;j++){
		input[i][j]=userInput.nextLong();
	    }
	//System.out.println("hello");
	for(int j=4;j>=0;j--){
	    for(int i=0;i<100;i++){
		System.out.println(i + "," + j);
		sum[j]=sum[j]+input[i][j];
	    }
	    //  System.out.println(j);
	    if(j>0){
		sum[j-1] = sum[j]/a;
		sum[j]=sum[j]%a;
	    }
	}
	System.out.println(sum[0]);
    }
}
