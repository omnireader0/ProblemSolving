// sol2 : bitCount 대신 함수 구현
public class Solution {
    public int solution(int n) {
        int count = countOne(n);         
        for(int i = n+1; ; i++){
            if(countOne(i) == count) return i;
        }
    }

    public int countOne(int n) {
        int cnt = 0;
        while(n>0) {
            if((n&1) == 1) cnt++;
            n >>= 1;
        }
        return cnt;
    }
}