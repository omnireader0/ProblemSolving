import java.util.*;
class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int cnt = 0;
        int[] students = new int[n+1];
        Arrays.fill(students, 1); 

        for (int i : reserve) students[i]++;
        for (int i : lost) students[i]--;

        for (int i = 1; i <= n; i++) {
            if (students[i] > 0) continue;

            if (students[i-1] > 1) {
                students[i-1]--;
                students[i]++;
                continue;
            }

            if(i < n && students[i+1] > 1) {
                students[i+1]--;
                students[i]++;
            }
        }
        // 강사님 방법 
        // return (int) Arrays.stream(students).filter(i -> i>0).count();

        for (int i = 1; i <= n; i++) {
            if (students[i] > 0) {
                cnt++;
            }
        }
        return cnt;
    }
}