package Java.Programmers.level1.K번째수.solution1;

import java.util.*;
public class Solution {
    public int[] solution(int[] array, int[][] commands){
        int[] answer = new int[commands.length];
        int idx = 0;
        for(int i=0; i<commands.length; i++){
            int start = commands[i][0];
            int end = commands[i][1];
            int k = commands[i][2];
            int l=0;
            int[] subArray = new int[end-start+1];
            for(int j=start-1; j<end; j++){
                subArray[l++] = array[j];
                            }
            Arrays.sort(subArray);
            answer[idx++]=subArray[k-1];
        }
        return answer;
    }
}