import java.util.*;
class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        Arrays.sort(times);

        // 심사기다리는 사람과 심사 시간은 1~10억이므로 long
        long left = 1; //  시간 1분 * 사람 1명
        long right = (long)times[times.length-1]*n;

        while (left <= right){

            long count = 0;
            long mid = (left+right)/2;

            for(int t: times){ 
                count += mid/t; 
            } // mid 시간동안 심사할 수 있는 사람의 수 : count

            if (count>=n){
                answer = mid;
                right = mid-1;
            }

            else
                left = mid + 1;
        }
        return answer;
    }
}