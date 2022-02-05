package Java.Programmers.level2.다음큰숫자.solution3;

public class Solution {
    public int solution(int n){
        int count = countOne(n);
        while(countOne(++n) != count);
        return n;
    }
    private int countOne(int n) {
        String bin = Integer.toBinaryString(n);
        int count = 0;
        // 1번
        for (int i = 0; i < bin.length(); i++) {
            String b = bin.substring(i, i+1);
            if (b.equals("1")) count++;
        }
        // 2번
        // for(char ch : bin.toCharArray()) {
        //     if(ch == '1') count++;
        // }
        return count;
    }
}