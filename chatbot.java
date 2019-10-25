import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class chatbot
{
	Map<String,String> welcome = new HashMap<String,String>();
	Map<String,String> chat = new HashMap<String,String>();
	Map<String,String> farewell = new HashMap<String,String>();
	public chatbot()
	{
		welcome.put("hi","Hello this is Robo. ");
		welcome.put("hey","Welcome to the firm. ");
		welcome.put("hello","Robo here. Welcome to the firm. ");
		
		chat.put("shares","You can purchase shares at the cost of Rs50 per share. ");
		chat.put("loan","For receiving a loan, you must provide certain documents. ");
		chat.put("bank","The bank has 3 branches in Pune. ");
		chat.put("invest","Investment is subject to market risks. Please read the scheme related documents carefully. ");
		chat.put("deposit","You can deposit a maximum amount of Rs 20,000. ");
		chat.put("withdrawl","You can withdraw a maximum amount of Rs 5000. ");
		
		farewell.put("Bye","Goodbye. ");
	}
	
	public String reply(String str)
	{
		String tokens[] = str.split("\\s");
		for(int i=0;i<tokens.length;i++)
		{
			if(welcome.containsKey(tokens[i].toLowerCase()))
				return welcome.get(tokens[i].toLowerCase());
			else if(chat.containsKey(tokens[i].toLowerCase()))
				return chat.get(tokens[i].toLowerCase());
			else if(farewell.containsKey(tokens[i].toLowerCase()))
				return farewell.get(tokens[i].toLowerCase());
		}
		return " ";
	}
	
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		chatbot c = new chatbot();
		String input;
		while(true)
		{
			input = sc.nextLine();
			System.out.println(c.reply(input));
		}
	}
	
}
