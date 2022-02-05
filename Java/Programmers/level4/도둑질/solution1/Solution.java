package Java.Programmers.level4.도둑질.solution1;

import java.util.*;
class Solution {
    public int solution(int[] money) {
        int length = money.length;
        int[] dp1 = new int[length]; 
        int[] dp2 = new int[length];
        
        // 첫 번째 집 털고, 두 번째 집 안터는 경우
        dp1[0] = money[0];
        dp1[1] = dp1[0];
        
        // 두 번째 집 털고, 첫 번째 집 안터는 경우
        dp2[0] = 0;
        dp2[1] = money[1];
        
        for(int i = 2; i < length; i++) {
            
            dp2[i] = Math.max(dp2[i-2]+money[i], dp2[i-1]);
            
            // 첫번째 집 터는 경우에는 마지막 집을 털면 안되므로
            if (i == length-1) continue;
            dp1[i] = Math.max(dp1[i-2]+money[i], dp1[i-1]);
            
        }
        return Math.max(dp1[length-2], dp2[length-1]);
    }
}