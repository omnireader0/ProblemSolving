package Java.Programmers.level2.타겟넘버.solution1;

import java.util.*;
class Solution {
    public int solution(int[] numbers, int target) {
        List<Integer> answer = new ArrayList<>();
        answer.add(0);
        for (int i=0; i<numbers.length; i++) {
            List<Integer> node = new ArrayList<>();
            for (int j=0; j<answer.size(); j++) {
                node.add(answer.get(j) - numbers[i]);
                node.add(answer.get(j) + numbers[i]);
            }
            answer = node;
        }
        int count = 0;
        for (int i: answer) {
            if (i==target) {
                count++;
            }
        }
        return count;
    }
}