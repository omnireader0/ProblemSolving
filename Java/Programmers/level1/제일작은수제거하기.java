package Java.Programmers.level1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class 제일작은수제거하기 {
    public static void main(String [] args){
        제일작은수제거하기 s = new 제일작은수제거하기();
        int [] arr = {10,1};
        System.out.println(Arrays.toString(s.solution(arr)));
    }
    // 버전 1
    // public int[] solution(int[] arr) {
    //     if (arr.length == 1){
    //         int [] answer = {-1};
    //         return answer;
    //     }
    //     int min = arr[0];
    //     for(int i=1; i<arr.length; i++){
    //         min = Math.min(min, arr[i]);
    //     }

    //     int [] answer = new int[arr.length-1];
    //     int idx = 0;
    //     for (int i = 0; i< arr.length; i++){
    //         if (arr[i]==min)
    //             continue;
    //         answer[idx ++] = arr[i];
    //     }
    //     return answer;
    // }   
    
    
    // 버전 2
    public int [] solution(int [] arr){
        if (arr.length ==1){
            arr[0] = -1;
            return arr;
        }
        else{
            ArrayList<Integer> arrayList = new ArrayList<Integer>();
            for (int a : arr){
                arrayList.add(a);
            }
            Integer min = Collections.min(arrayList);
            arrayList.remove(min);
            int [] result = new int[arr.length-1];
            for(int i=0; i<arrayList.size(); i++){
                result[i]= arrayList.get(i);
            }
            return result;
        }
    }
}
