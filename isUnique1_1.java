public class isUnique1_1{
	public static void main(String[] args){
		System.out.println("result is: " + isUniqueChars("abcdeh"));
	}


	public static boolean isUniqueChars(String str){
	if(str.length() > 128) return false;
	boolean[] chArr = new boolean[128];

	for(int i=0; i<str.length(); i++){
		int val = str.charAt(i);

		if(chArr[val]) return false;
		chArr[val] = true;
	}

	return true;

	}
}
