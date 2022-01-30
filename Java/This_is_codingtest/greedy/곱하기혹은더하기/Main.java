package Java.This_is_codingtest.greedy.곱하기혹은더하기;

import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        
        // long : string이 사이즈가 20인 경우, 숫자로 변환시 커짐
        long answer = str.charAt(0) - '0';

        for (int i=1; i<str.length(); i++) {
            int num = str.charAt(i) - '0';
            if (num <= 1 || answer <= 1) {
                answer += num;
            }
            else{
                answer *= num;
            }
        }
        System.out.println(answer);
    }
}
