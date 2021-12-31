package Java.Programmers.level1;
import java.util.Arrays;
public class 로또의최고순위와최저순위2 {
public static void main(String [] args){
    로또의최고순위와최저순위2 s = new 로또의최고순위와최저순위2();
    int [] lottos = {44, 1, 0, 0, 31, 25};
    int [] win_nums = {31, 10, 45, 1, 6, 19};
    System.out.println(Arrays.toString(s.solution(lottos, win_nums)));
}

    public int[] solution(int[] lottos, int[] win_nums) {
        int [] answer = {0,0};
        int zero = 0;
        int cnt = 0;
        for(int l : lottos){
            if (l==0) zero++;
            else {
                for (int w : win_nums){
                    if(l==w){
                        cnt ++;
                        break;
                    }
                }
            }
        }
        int min = cnt;
        int max = zero + cnt;
        answer[0] = Math.min(7-max, 6);
        answer[1] = Math.min(7-min, 6);
        return answer;
}
}

/**
 * 테스트 1 〉	통과 (0.04ms, 72.6MB)
테스트 2 〉	통과 (0.03ms, 77.3MB)
테스트 3 〉	통과 (0.04ms, 73.9MB)
테스트 4 〉	통과 (0.04ms, 76.8MB)
테스트 5 〉	통과 (0.04ms, 77.1MB)
테스트 6 〉	통과 (0.03ms, 80.6MB)
테스트 7 〉	통과 (0.03ms, 76.5MB)
테스트 8 〉	통과 (0.03ms, 72.6MB)
테스트 9 〉	통과 (0.02ms, 74.4MB)
테스트 10 〉	통과 (0.04ms, 76.6MB)
테스트 11 〉	통과 (0.03ms, 72.8MB)
테스트 12 〉	통과 (0.03ms, 79.8MB)
테스트 13 〉	통과 (0.03ms, 79.8MB)
테스트 14 〉	통과 (0.02ms, 76.7MB)
테스트 15 〉	통과 (0.03ms, 73.5MB)
 */


 /* 
 다른 풀이

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        Map<Integer, Boolean> map = new HashMap<Integer, Boolean>();
        int zeroCount = 0;

        for(int lotto : lottos) {
            if(lotto == 0) {
                zeroCount++;
                continue;
            }
            map.put(lotto, true);
        }


        int sameCount = 0;
        for(int winNum : win_nums) {
            if(map.containsKey(winNum)) sameCount++;
        }

        int maxRank = 7 - (sameCount + zeroCount);
        int minRank = 7 - sameCount;
        if(maxRank > 6) maxRank = 6;
        if(minRank > 6) minRank = 6;

        return new int[] {maxRank, minRank};
    }
}

테스트 1 〉	통과 (0.04ms, 80.2MB)
테스트 2 〉	통과 (0.04ms, 73MB)
테스트 3 〉	통과 (0.05ms, 73.8MB)
테스트 4 〉	통과 (0.02ms, 75.6MB)
테스트 5 〉	통과 (0.04ms, 75.5MB)
테스트 6 〉	통과 (0.03ms, 75.2MB)
테스트 7 〉	통과 (0.03ms, 66.3MB)
테스트 8 〉	통과 (0.04ms, 74.8MB)
테스트 9 〉	통과 (0.05ms, 77.3MB)
테스트 10 〉	통과 (0.04ms, 69.9MB)
테스트 11 〉	통과 (0.03ms, 75.2MB)
테스트 12 〉	통과 (0.04ms, 81MB)
테스트 13 〉	통과 (0.04ms, 74.5MB)
테스트 14 〉	통과 (0.03ms, 77MB)
테스트 15 〉	통과 (0.02ms, 75.6MB)
 */