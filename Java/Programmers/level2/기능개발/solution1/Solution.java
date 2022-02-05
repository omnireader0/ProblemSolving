import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> list = new ArrayList<Integer>();
        int[] answer = {};
        int size = progresses.length;
        int count = 1;
        int max = -1;
        
        for (int i=0; i<size; i++){
            int days = (100-progresses[i])/speeds[i] + ((100 - progresses[i])%speeds[i]>0?1:0);
            
            if (i==0) {
                max = days;
                continue;
            }
            
            if (max >= days){
                count++;
                continue;
            }
            
            list.add(count);
            max = days;
            count = 1;
        }

        list.add(count);
        //answer = list.stream().mapToInt(i->i).toArray();
        answer = new int[list.size()];
        for (int i=0; i<answer.length; i++){
            answer[i] = list.get(i).intValue();
        }
        return answer;
    }
}