package tryit;

import java.util.Arrays;

public class que11 {
	
	public int[] missing(int[] a){
		int[] b = new int[100];
		int i = 0;
		int j =0;
		while ( i < 100){
			
			if(Arrays.asList(a).contains(i)){
			}
			else{
				b[j] = i;
				j ++;
			}
			i ++;
		}
		
		
		return b;
		
	}
	public static void main(String s[]){

		
		int[] a =new int[]{2,3,4,5,6,7};
		que11 n = new que11();
		int[] c =n.missing(a);
		for(int i:c){
			System.out.println(i);
		}
		
	}
}
