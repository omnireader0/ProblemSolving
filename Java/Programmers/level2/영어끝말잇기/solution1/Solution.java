import java.util.*;
public class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = new int[2];
        List<String> list = new ArrayList<>();
        list.add(words[0]);
        for(int i=1; i<words.length; i++){
            String last = list.get(list.size()-1);
            String now = words[i];
            if(!list.contains(now) && last.charAt(last.length()-1) == now.charAt(0)){
                list.add(now);
            }
            else{
                answer[0] = i%n+1;
                answer[1] = i/n+1;
                return answer;
            }
        }
        return answer;
    }
}