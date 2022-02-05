package Java.Programmers.level2.다음큰숫자.solution1;

public class Solution {
    public int solution(int n) {
        int cnt = Integer.bitCount(n);
        for(int i = n+1; ; i++){
            if (Integer.bitCount(i) == cnt) return i;
        }
    }
}