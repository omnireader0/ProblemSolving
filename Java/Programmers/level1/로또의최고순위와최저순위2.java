package Java.Programmers.level1;
import java.util.Arrays;
public class 로또의최고순위와최저순위2 {
public static void main(String [] args){
    로또의최고순위와최저순위2 s = new 로또의최고순위와최저순위2();
    int [] lottos = {44, 1, 0, 0, 31, 25};
    int [] win_nums = {31, 10, 45, 1, 6, 19};
    System.out.println(Arrays.toString(s.solution(lottos, win_nums)));
}

    public int[] solution(int[] lottos, int[] win_nums) {
        int [] answer = {0,0};
        int zero = 0;
        int cnt = 0;
        for(int l : lottos){
            if (l==0) zero++;
            else {
                for (int w : win_nums){
                    if(l==w){
                        cnt ++;
                        break;
                    }
                }
            }
        }
        int min = zero;
        int max = zero + cnt;
        answer[0] = Math.min(7-max, 6);
        answer[1] = Math.min(7-min, 6);
        return answer;
}
}
