package Java.Programmers.level1;

import javax.lang.model.util.ElementScanner14;

public class 콜라츠추측 {
    public static void main(String [] args){
        콜라츠추측 s = new 콜라츠추측();
        System.out.println(s.solution(626331));
    }
    public int solution(long num) {
        int answer = 0;
        while (answer<500 && num!=1){
            if(num%2==0)
                num = num/2;
            else
                num = num*3 + 1;
            answer ++;
        }
        if (num!=1)
            return -1;
        else
            return answer;
    }
}

// long으로 놓고 풀어야 한다.
// int의 경우 21억을 넘으면 연산값 제한으로 계산 오류 발생