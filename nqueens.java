import java.util.*;
public class nqueens
{
	public boolean solvenq(int n)
	{
		int board[][] = new int[n][n];
		
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				board[i][j]=0;
				
		if(nq(board,0,n) == false)
		{
			System.out.println("Solution does not exist");
			return false;
		}
		printBoard(board,n);
		return true;
	}
	
	public boolean nq(int board[][], int col, int n)
	{
		if(col>=n)
			return true;
		
		for(int i=0;i<n;i++)
		{
			if(isSafe(board,i,col,n))
			{
				board[i][col]=1;
				if(nq(board,col+1,n) == true)
					return true;			
			
				board[i][col] =0;
			}
		}
		return false;
	}
	
	public boolean isSafe(int board[][],int row,int col, int n)
	{
		int i,j;
		//left row
		for(i=0;i<col;i++)
			if(board[row][i] == 1)
				return false;
		//left upper diagonal
		for(i=row, j=col;i>=0 && j>=0;i--,j--)
			if(board[i][j] == 1)
				return false;
				
		//left lower diagonal
		for(i=row,j=col;i<n && j>=0;i++,j--)
			if(board[i][j] == 1)
				return false;
		
		return true;
	}
	
	public void printBoard(int board[][], int n)
	{
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
				System.out.print(board[i][j]);
			System.out.println();
		}
	}
	
	public static void main(String args[])
	{
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		nqueens nq = new nqueens();
		nq.solvenq(n);
	}
}
