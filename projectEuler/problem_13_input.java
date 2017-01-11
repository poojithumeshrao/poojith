import java.io.DataInputStream;
import java.io.PrintWriter;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
public class problem_13_input{
    public static void main(String[] args){
	File f=new File("problem_13_input.txt");
	File f1=new File("problem_13_output.txt");
	try{
	    PrintWriter out = new PrintWriter("problem_13_output.txt");
	    
	    String[] temp = new String[5];
	    BufferedReader reader = new BufferedReader(new InputStreamReader(new DataInputStream(new FileInputStream(f))));
	    for (String line ; (line = reader.readLine()) != null;){
		temp = line.split("(?<=\\G.{10})");
			for(int z=0;z<5;z++){
		    System.out.println(temp[z]);
			}
	    }
	}
	catch (Exception e ){}
		/*	try {
			BufferedWriter bufwriter = new BufferedWriter(new FileWriter(f1));
			bufwriter.write("hello");//writes the edited string buffer to the new file
			//bufwriter.close();//closes the file
			} catch (Exception e) {//if an exception occurs
			System.out.println("Error occured while attempting to write to file: " + e.getMessage());
			}
			}
	    }
	    catch(FileNotFoundException ex){
	    }
	    catch(Exception e){
	    System.out.println("ERROR");
	    }
	    finally {
	    f.close();
	    f1.close();
	    System.out.println("some error");
	    }*/
    }
}
    

	
