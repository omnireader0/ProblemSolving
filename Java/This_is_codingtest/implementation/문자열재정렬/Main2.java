package Java.This_is_codingtest.implementation.문자열재정렬;
import java.util.*;
public class Main2 {
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);
        String s = sc.next();

        String alpha = "";
        int number = 0;
        for (int i=0; i<s.length(); i++) {
            if(Character.isDigit(s.charAt(i))) {
                number += s.charAt(i) - '0';
            }
            else alpha += s.charAt(i);
        }
        char[] answer = alpha.toCharArray();
        Arrays.sort(answer);
        
        System.out.print(String.valueOf(answer));
        if (number != 0) System.out.print(String.valueOf(number));
    }
}
