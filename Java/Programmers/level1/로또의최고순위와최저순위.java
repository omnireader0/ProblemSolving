package Java.Programmers.level1;

import java.util.Arrays;

/*
1. 로또와 당첨 배열 정렬
2. 로또의 0의 개수 세기
3. 두 배열의 일치하는 원소 개수 세기
*/ 
class 로또의최고순위와최저순위 {
    
    public static void main(String [] args){
        로또의최고순위와최저순위 s = new 로또의최고순위와최저순위();
        int [] lottos = {44, 1, 0, 0, 31, 25};
        int [] win_nums = {31, 10, 45, 1, 6, 19};
        System.out.println(Arrays.toString(s.solution(lottos, win_nums)));

    }

    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = {0,0};
        int zeroCnt = 0;
        int cnt = 0;

        Arrays.sort(lottos);
        Arrays.sort(win_nums);

        for (int i=0; i<6; i++){
            if (lottos[i]==0){
                zeroCnt += 1;
            }
        }
        for (int i=zeroCnt; i<6; i++){
            for (int j =0; j<6; j++){
                if (lottos[i]== win_nums[j]){
                    cnt += 1;
                }
            }
        }
        if (cnt + zeroCnt == 6) answer[0]= 1;
        else if (cnt + zeroCnt == 5) answer[0]= 2;
        else if (cnt + zeroCnt == 4) answer[0]= 3;
        else if (cnt + zeroCnt == 3) answer[0]= 4;
        else if (cnt + zeroCnt == 2) answer[0]= 5;
        else answer[0] = 6;

        if (cnt ==  6) answer[1] = 1;
        else if (cnt == 5) answer[1] = 2;
        else if (cnt == 4) answer[1] = 3;
        else if (cnt == 3) answer[1] = 4;
        else if (cnt == 2) answer[1] = 5;
        else  answer[1] = 6;
        return answer;
    }
}