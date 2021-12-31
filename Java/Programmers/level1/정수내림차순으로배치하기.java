package Java.Programmers.level1;
import java.lang.String;
import java.util.*;
public class 정수내림차순으로배치하기 {
    public static void main(String [] args ){
        정수내림차순으로배치하기 s = new 정수내림차순으로배치하기();
        System.out.println(s.solution(118372));
        }
        public long solution(long n){
            String answer ="";
            // Long to String 
            String str = Long.toString(n);
            // split 하기
            String [] numbers = str.split("");
            // 오름차순
            Arrays.sort(numbers);
            // 문자열 만들기
            for (int i=numbers.length-1; i>=0; i--){
                answer += numbers[i];
            }
            // 문자열을 숫자로 형변환
            long final_answer = Long.parseLong(answer);
            return final_answer;
    }

    // 나중에 공부하기..

//     public long solution(long n) {
//         String[] list = String.valueOf(n).split("");
//         Arrays.sort(list);

//         StringBuilder sb = new StringBuilder();
//         for (String aList : list) sb.append(aList);

//         return Long.parseLong(sb.reverse().toString());
//   }
}
