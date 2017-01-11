public  class smal{
    void small(){
    }
    long  hcf(long x,long y){
	long rem = x%y;
	while(rem != 0){
	    x=y;
	    y=rem;
	    rem=x%y;
	}
	return y;
    } 
	    
    public static void main(String args[]){
	smal s = new smal();
	long  minProd=6;
	for(int i=4;i<=20;i++)
	    {
		minProd = (minProd*i)/s.hcf(minProd,i);
	    }
	System.out.println(minProd);
    }
}
	
