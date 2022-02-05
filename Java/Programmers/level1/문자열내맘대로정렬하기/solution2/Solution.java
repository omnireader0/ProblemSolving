package Java.Programmers.level1.문자열내맘대로정렬하기.solution2;
import java.util.*;
// sol 2-1 Arrays.sort 하면서 custom 구현된 Comparator 객체를 넣는 방법

class Solution {
    public String[] solution(String[] strings, int n) {
        
        Comparator CustomComparator = new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                if (s1.charAt(n) == s2.charAt(n))
                    return s1.compareTo(s2);
                else 
                    return s1.charAt(n) - s2.charAt(n);       
            }
        };
        Arrays.sort(strings, CustomComparator);
        return strings;
    }
}