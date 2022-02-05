import java.util.*;
public class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = new int[2];
        Set<String> set = new HashSet<>();
        set.add(words[0]);
        String last = words[0];
        for(int i=1; i<words.length; i++){
            String now = words[i];
            if(!set.contains(now) && last.charAt(last.length()-1) == now.charAt(0)){
                set.add(now);
                last = now;
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