import java.util.*;
public class problem_16{
    final int n = 10;
    public static void main(String args[]){	
	int sum,i,j,temp,carry;
	i=1;
	ArrayList<Integer> num = new ArrayList<Integer>();
	num.add(2);
	for( i =0;i<350;i++)
	    num.add(0);
	i=0;
	//System.out.println(num.get(0));
	while(i<999){
	    j=0;
	    carry=0;
	    while(j<=num.size() -1){
		temp = num.get(j);
		temp = temp*2;	
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

	
