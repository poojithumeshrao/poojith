import java.util.*;
public class problem_20{
    final int n = 10;
    public static void main(String args[]){	
	int sum,i,j,temp,carry;
	i=1;
	ArrayList<Integer> num = new ArrayList<Integer>();
	num.add(1);
	for( i =0;i<350;i++)
	    num.add(0);
	i=1;
	//System.out.println(num.get(0));
	while(i<100){
	    j=0;
	    carry=0;
	    while(j<=num.size() -1){
		temp = num.get(j);
		temp = temp*i;	
		temp=temp+carry;
		carry=temp/10;
		temp=temp%10;
		//	if(num.size()>1);
		//System.out.println(j +"  " + num.get(j));
			num.remove(j);
		num.add(j,temp);
		//System.out.println(j +"  " + num.get(j));
		j++;
		//	System.out.println(num.size());
		}
	    i++;
	    //    System.out.println(j +"  " + num.get(j));
	}
	
	sum=0;
	for(i=0;i<num.size();i++)
	    sum=sum+num.get(i);
	
System.out.println(sum);
    }
}
