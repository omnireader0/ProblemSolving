import java.util.*;
public class Solution {
    public int[] solution(int[] array, int[][] commands){
        int [] answer = new int[commands.length];
        int idx = 0;
        for(int i=0; i<commands.length; i++){
            int start = commands[i][0];
            int end = commands[i][1];
            int k = commands[i][2];
            int[] subArray = Arrays.copyOfRange(array, start-1, end);
            Arrays.sort(subArray);
            answer[idx++] = subArray[k-1];
        }
        return answer;
    }
}