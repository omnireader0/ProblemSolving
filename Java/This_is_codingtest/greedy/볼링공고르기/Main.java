package This_is_codingtest.볼링공고르기;
import java.util.*;
public class Main {
    
    public static int[] balls = new int[11];
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        for (int i = 0; i<n; i++) {
            int x = sc.nextInt();
            balls[x] += 1;
        }

        int answer = 0;
    
        for (int i=0; i<m; i++) {
            n -= balls[i];
            answer += balls[i] * n;
        }
        
        System.out.println(answer);
    }
}
