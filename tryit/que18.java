package tryit;

public class que18 {
	public int[] reverse(int[] a){
		int size = a.length -1;
		int[] b= new int[a.length];
		int i = 0;
		while (size  >= 0){
			b[i] = a[size];
			size --;
			i ++;
		}
		return b;
		
	}
	
	
public static void main(String s[]){

	
	int[] a =new int[]{2,3,4,5,6,7};
	que18 n = new que18();
	int[] c =n.reverse(a);
	for(int i:c){
		System.out.println(i);
	}
	
}

}
