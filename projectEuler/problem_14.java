public class problem_14{
    public static void main(String[] args){
	long count,max,i,r,val;
	int flag=1;
	
	//	long[] seqCount= new long[100000000];
	//	seqCount[1]= -1;
	max = 0;
	r=0;
	for(i=2;i<=1000000;i++){
	    val = i;
	    count=0;
	    while(true){
		if(val%2==0){
		    val = val/2;
		    count++;
		    /*   if(seqCount[val] > 0){
			count = count+seqCount[val];
			break;
			}*/
		}
		else if(val != 1) {
		    val = 3*val + 1;
		    count++;
		    /*if(seqCount[val] > 0){
			count = count + seqCount[val];
			break;
			}*/
		}
		else
		    break;
	    }
	    // seqCount[i]=count;		
	    if(max<count){
		max = count;
		r=i;
	    }
	    // System.out.println(i);
	}
	//	for(i=0;i<10;i++)
	    System.out.println(r + "   " + max);	
    }
}
	
