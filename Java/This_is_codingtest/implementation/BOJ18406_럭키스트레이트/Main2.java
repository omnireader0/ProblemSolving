package Java.This_is_codingtest.implementation.BOJ18406_럭키스트레이트;
import java.util.*;
import java.util.stream.IntStream;
public class Main2 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        String[] numbers = String.valueOf(n).split("");
        
        int l = numbers.length;

        int left = IntStream.range(0, l/2).map(i-> Integer.parseInt(numbers[i])).sum();
        int right = IntStream.range(l/2, l).map(i-> Integer.parseInt(numbers[i])).sum();

        System.out.println(left == right ? "LUCKY" : "READY");
    }
    
}
