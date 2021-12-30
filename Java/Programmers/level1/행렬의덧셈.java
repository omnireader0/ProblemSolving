package Java.Programmers.level1;

import java.util.Arrays;

public class 행렬의덧셈 {
    public static void main(String [] args){
        행렬의덧셈 s = new 행렬의덧셈();
        int [][] arr1 =  {{1,2},{2,3}};
        int [][] arr2 = {{3,4}, {5,6}};
        //System.out.println(Arrays.toString(s.solution(arr1, arr2)));
        //[[I@7a81197d  -> 배열 안에 있는 배열을 가리키는 주소값
        System.out.println(Arrays.deepToString(s.solution(arr1,arr2)));
    }
    // 버전 1
    // public int[][] solution(int [][] arr1, int[][] arr2){
    //     int[][] answer = new int[arr1.length][arr1[0].length];
    //     for (int i=0; i<arr1.length; i++){
    //         for (int j=0; j<arr1[0].length; j++){
    //             answer[i][j] = arr1[i][j] + arr2[i][j];
    //          }
    //     }
    //     return answer;
    // }

    // 버전 2
    public int [][] solution(int [][] arr1, int[][] arr2){
        int [][] answer = arr1;
        for (int i=0; i<arr1.length; i++){
            for (int j=0; j<arr1[0].length; j++){
                answer[i][j] += arr2[i][j];
            }
        }
        return answer;
    }
}
