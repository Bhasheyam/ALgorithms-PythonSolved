package tryit;

public class instance {
	public int[] instances(int[] a){
		int[] ans = new int[2];
		int ansin = -1;
		int temp = -1;
		int ansd = a.length;
		int count = 0;
		boolean flag = false;
		
		for ( int i = 0; i < a.length; i++ )
		 {
			
			if( a[i] == 5 & flag == false){
				temp = i;
				flag = true;	
			}
			else if(a[i] == 7 & flag == true){
				if(count < ansd){
					ansd = count;
					ansin = temp;
					flag = false;
				}
			}
				else if(flag == true){
					
					count = count +  1;
				}
				
			}
		
		ans[0] = ansin;
		ans[1] = ansd;
		return ans;
		
	}
public static void main(String s[]){

		
		int[] a =new int[]{2,3,4,5,6,7,5,6,6,8,9,7};
		instance n = new instance();
		int[] c =n.instances(a);
		for(int i:c){
			System.out.println(i);
		}
		
	}
}
