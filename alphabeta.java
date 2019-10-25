import java.util.*;
import java.io.*;
public class alphabeta
{
	static int min = Integer.MIN_VALUE;
	static int max = Integer.MAX_VALUE;
	static int max_dep = 3;
	int prune(int depth, int nodeindex, int values[], boolean maxplayer, int alpha, int beta)
	{
		if (depth ==max_dep)
			return values[nodeindex];
		else if(maxplayer)
		{
			int best = min;
			for(int i=0;i<2;i++)
			{
				int val = prune(depth+1, nodeindex*2 +i,values, false, alpha, beta);
				best = Math.max(best,val);
				alpha = Math.max(alpha, best);
				
				if(beta<=alpha)
					break;
			}
			return best;
		}
		else
		{
			int best=max;
			for(int i=0;i<2;i++)
			{
				int val = prune(depth+1,nodeindex*2 +i,values,true,alpha,beta);
				best = Math.min(best,val);
				beta = Math.min(best,beta);
				
				if(beta<=alpha)
					break;
			}
			return best;
		}
	}
	public static void main(String args[])
	{
		alphabeta ab = new alphabeta();
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter max depth");
		int dep = sc.nextInt();
		System.out.println("Enter elements of the array");
		int val = (int) Math.pow(2,dep);
		int arr[] = new int[val];
		max_dep = dep;
		for(int i=0;i<val;i++)
			arr[i]=sc.nextInt();
		//int arr[]={3,5,6,9,1,2,0,-1};
		System.out.println(ab.prune(0,0,arr,true,min,max));
	}
}
