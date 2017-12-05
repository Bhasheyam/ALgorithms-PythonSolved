package tryit;

public class arrayque {
	
	public static void main(String s[]){
		
		
		int[][] a = new int[100][100];
		int[] ans = new int[200];
		int k = 0;
		
	for(int i = 0; i < a.length; i++){
        for (int j = 0; j < a[i].length; j++){
            ans[k] = a[i][j];
            k ++; 
        }
    }
}
}
