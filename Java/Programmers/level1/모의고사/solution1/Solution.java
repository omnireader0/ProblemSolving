package Java.Programmers.level1.모의고사.solution1;

import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
        List<Integer> result = new ArrayList<Integer> ();
        int[] number1 = {1, 2, 3, 4, 5};
        int[] number2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] number3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int cnt1 = 0, cnt2 = 0, cnt3 = 0;
        for(int i=0; i<answers.length; i++){
            if(answers[i] == number1[i%5]){
                cnt1 ++;
            }
            if(answers[i] == number2[i%8]){
                cnt2 ++;
            }
            if(answers[i] == number3[i%10]){
                cnt3 ++;
            }
        }
        int maxCnt = (cnt1>cnt2)&&(cnt1>cnt3)?cnt1:(cnt3>cnt2?cnt3:cnt2);
        if (maxCnt==cnt1) result.add(1);
        if (maxCnt==cnt2) result.add(2);
        if (maxCnt==cnt3) result.add(3);

        int [] answer= new int[result.size()];
        for(int i=0; i<result.size(); i++){
            answer[i] = result.get(i);
        }
        return answer;
    }
}