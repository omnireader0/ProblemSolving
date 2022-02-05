package Java.This_is_codingtest.implementation.문자열재정렬;

import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String s = sc.next();

        int number = 0;
        List<Character> list = new ArrayList<>();

        for(int i=0; i<s.length(); i++) {
            if( '0'<= s.charAt(i) && s.charAt(i) <= '9') {
                number += s.charAt(i) - '0';
            }
            else list.add(s.charAt(i));
        }

        Collections.sort(list);
        
        if (number != 0) list.add(Character.forDigit(number, 10));

        for(int i=0; i<list.size(); i++) {
            System.out.print(list.get(i));
        }
    }
}
