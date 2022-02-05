public class Solution {
    public int solution(int n) {	    public int solution(int n) {
        int answer = 0;	        int cnt = Integer.bitCount(n);
        return answer;	        for(int i = n+1; ; i++){
            if (Integer.bitCount(i) == cnt) return i;
        }
    }	    }
}	}
