public class problem_19{
    public static void main(String[] args){
	int year,day,sum;
	int count =0;
	year = 1901;
	sum=2;
	int[]month = {31,28,31,30,31,30,31,31,30,31,30,31};
	while(year<=2000){
	    for(int i=0;i<12;i++){
		if((year%400==0 || (year%4==0 && year%100!=0)) && i==1)
		    sum = sum + 29;
		else
		    sum=sum+month[i];
		sum = sum % 7;
		if(sum==0)
		    count++;
	    }
	    year++;
	}
	System.out.println(count);
    }
}
