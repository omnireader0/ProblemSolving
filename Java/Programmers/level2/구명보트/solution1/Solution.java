package Java.Programmers.level2.구명보트.solution1;

import java.util.*;
class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        Arrays.sort(people);
        int left = 0;
        int right = people.length -1;
        while(left <= right) {
            if (people[left] + people[right] > limit){
                answer+= 1;
                right -= 1;
            }
            else {
                left += 1;
                right -= 1;
                answer+= 1;
            }
        }
        return answer;
    }
}