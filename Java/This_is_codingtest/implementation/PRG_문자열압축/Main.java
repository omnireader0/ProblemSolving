package Java.This_is_codingtest.implementation.PRG_문자열압축;
import java.util.*;
public class Main {
    public int solution(String s) {
        int answer = s.length();
        for (int i=1; i<s.length()/2+1; i++){
            String comp = "";
            String prev = s.substring(0, i);
            int cnt = 1;
            for (int j=i; j<s.length(); j+=i) {
                
                String subStr = "";
                subStr = ( j+i<s.length()) ? s.substring(j, j+i) : s.substring(j, s.length());
                
                if (prev.equals(subStr)) cnt++;
                else {
                    if (cnt==1) comp += prev;
                    else comp += cnt + prev;
                    subStr = ( j+i<s.length()) ? s.substring(j, j+i) : s.substring(j, s.length());
                    prev = subStr;
                    cnt = 1;
                }
            }
            comp += (cnt >= 2)? cnt + prev : prev;
            answer = Math.min(answer, comp.length());
        }
        return answer;
    }
}
