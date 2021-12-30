package Java.Programmers.level1;
import java.util.Arrays;
public class x만큼간격이있는n개의숫자 {
    public static void main(String[] args){
        x만큼간격이있는n개의숫자 s = new x만큼간격이있는n개의숫자();
        int x = -4;
        int y = 2;
        System.out.println(Arrays.toString(s.solution(x,y)));
    }
    //버전 1
    public long[] solution(int x, int n) {
        long [] answer = new long[n];
        for (int i=1; i<=n; i++){
            answer[i-1] = (long)x*i;
        }
        return answer;
    }

    // 버전 2
//     public static long[] solution(int x, int n){
//         long [] answer = new long[n];
//         answer[0] = x;
//         for (int i=1; i<n; i++){
//             answer[i] = answer[i-1] + x;
//         }
//         return answer;
//      }
}
