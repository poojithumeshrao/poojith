import java.util.Scanner;
public class problem_18{
    public static void main(String[] args){
	int[][] input = new int[20][20];
	Scanner in = new Scanner(System.in);
	int i,j;
	for(i=0;i<15;i++){
	    for(j=0;j<i+1;j++){
		input[i][j]=in.nextInt();
	    }
	}
	
	for(i=13;i>=0;i--){
	    for(j=0;j<i+1;j++){
		if(input[i+1][j]>input[i+1][j+1])
		    input[i][j]=input[i][j]+input[i+1][j];
		else
		    input[i][j]=input[i][j]+input[i+1][j+1];
	    }
	}
	//System.out.println(input[0][0]);
	for(i=0;i<15;i++){
	    for(j=0;j<i+1;j++){
		System.out.print(input[i][j] + "  ");
	    }
	    System.out.println();
	    }
    }
}
