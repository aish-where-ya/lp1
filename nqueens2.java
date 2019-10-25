import java.util.*;
public class nqueens2
{
	void printblock(int block[][], int n)
	{
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
				System.out.print(block[i][j]);
			System.out.println();
		}
	}
	boolean solvenq(int n)
	{
		int board[][]= new int[n][n];
		boolean slashcodelookup[]= new boolean[2*n -1];
		//Arrays.fill(slashcodelookup, boolean.FALSE);
		boolean backslashcodelookup[] = new boolean[2*n -1 ];
		//Arrays.fill(backslashcodelookup, boolean.FALSE);
		boolean rowlookup[]= new boolean[n];
		//Arrays.fill(rowlookup, boolean.FALSE);
		
		int slashcode[][] = new int[n][n];
		int backslashcode[][] = new int[n][n];
		
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
			{
				slashcode[i][j]=i+j;
				backslashcode[i][j]=i-j+n-1;
			}
		}
		
		if(nq(board,n,0,slashcode,backslashcode,rowlookup,slashcodelookup,backslashcodelookup) ==false)
		{
			System.out.println("Solution does not exist");
			return false;
		}
		printblock(board,n);
		return true;
	} 
	boolean nq(int board[][], int n, int col, int slashcode[][], int backslashcode[][], boolean rowlookup[], boolean slashcodelookup[], boolean backslashcodelookup[])
	{
		if(col>=n)
			return true;
		
		for(int i=0;i<n;i++)
		{
			if(isSafe(i,col,slashcode, backslashcode,rowlookup, slashcodelookup, backslashcodelookup))
			{
				board[i][col]=1;
				rowlookup[i]= true;
				slashcodelookup[slashcode[i][col]]=true;
				backslashcodelookup[backslashcode[i][col]]=true;
				
				if(nq(board,n,col+1,slashcode,backslashcode,rowlookup,slashcodelookup,backslashcodelookup)==true)
					return true;
				
				board[i][col]=0;
				rowlookup[i]= false;
				slashcodelookup[slashcode[i][col]]=false;
				backslashcodelookup[backslashcode[i][col]]=false;
				
			}
		}
		return false;
	}
	
	boolean isSafe(int row, int col,int slashcode[][], int backslashcode[][], boolean rowlookup[], boolean slashcodelookup[], boolean backslashcodelookup[])
	{
		if(rowlookup[row] || slashcodelookup[slashcode[row][col]] || backslashcodelookup[backslashcode[row][col]])
			return false;
		return true;
	}
	
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		nqueens2 obj = new nqueens2();
		obj.solvenq(n);
	}
}
