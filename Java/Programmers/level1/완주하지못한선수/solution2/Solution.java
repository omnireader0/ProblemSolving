package Java.Programmers.level1.완주하지못한선수.solution2;

import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Map<String, Integer> players = new HashMap<>();

        for (String p : participant) {
            players.put(p, players.getOrDefault(p, 0) + 1);
        }

        for (String c : completion) {
            players.put(c, players.get(c)-1);
        }

        for (Map.Entry<String, Integer> entry : players.entrySet()) {
            if (entry.getValue() == 1) {
                answer = entry.getKey();
                break;
            }
        }
        return answer;
    }
}