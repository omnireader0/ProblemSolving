package Java.This_is_codingtest.implementation.BOJ18406_럭키스트레이트;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String n = sc.next();

        int count = n.length();

        String s1 = n.substring(0, count/2);
        String s2 = n.substring(count/2, count);
        
        int left_sum = 0;
        int right_sum = 0;

        for (int i=0; i<count/2; i++) {
            left_sum += s1.charAt(i) - '0';
            right_sum += s2.charAt(i) - '0';
        }
        
        if(left_sum == right_sum) System.out.println("LUCKY");
        else System.out.println("READY");
    }
}
