import java.util.*;
class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> map = new HashMap<>();
        for (String [] c : clothes) {
            String key = c[1];
            map.put(key, map.getOrDefault(key, 0)+1);
        }
        for (String key : map.keySet()) {
            answer *= (map.get(key)+1);
        }
        return answer-1;
    }
}