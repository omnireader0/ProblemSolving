package Java.Programmers.level1.문자열내맘대로정렬하기.solution1;

import java.util.*;
public class Solution {
    public String[] solution(String[] strings, int n) {
        String[] answer = new String[strings.length];
        ArrayList<String> array = new ArrayList<String>();
        for(int i=0; i<strings.length; i++){
            array.add(strings[i].charAt(n) + strings[i]);
        }
        Collections.sort(array);
        for(int i=0; i<array.size(); i++){
            answer[i] = array.get(i).substring(1);
        }
        return answer;
    }
}