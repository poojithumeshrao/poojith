public class split{
    public static void main(String[] args){
	String temp = "1234567890";
	String[] ans = new String[10];
	ans = temp.split("(?<=\\G.{2})");
	for(int i=0;i<5;i++)
	    System.out.println(ans[i]);
    }
}
