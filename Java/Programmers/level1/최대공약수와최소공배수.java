package Java.Programmers.level1;

import java.util.Arrays;

public class 최대공약수와최소공배수 {
    
    public static void main(String [] args){
        최대공약수와최소공배수 s = new 최대공약수와최소공배수();
        System.out.println(Arrays.toString(s.solution(3,12)));
    }
    // 버전 1 : while 
    // public int[] solution(int n, int m){
    //     int [] answer = new int[2];
    //     int temp = 1;
    //     int gcd = n*m;
    //     while (temp != 0){
    //         temp = n%m;
    //         n = m;
    //         m = temp;
    //     }
    //     answer[0] = n;
    //     answer[1] = gcd/n;
    //     return answer;
    // }

    // 버전 2 : 재귀
    public int [] solution(int n, int m){
        int [] answer = {0,0};
        int big, small;
        if (m>n){
            big = m; small =n;
        }
        else {
            big = n; small = m;
        }
        answer[0] = gcd(big, small);
        answer[1] = n*m/answer[0];
        return answer;
    }
    public int gcd(int a, int b){
        if(a%b ==0)
            return b;
        return gcd(b, a%b);
    }
}
