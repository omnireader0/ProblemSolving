### [문제](https://programmers.co.kr/learn/courses/30/lessons/42748)

### 풀이 1
문제에서 제시한 순서대로 구현했습니다.

1. command에 따라 자른 배열을 서브 배열에 담고, 정렬
2. 서브 배열의 k번째 수를 answer에 담아서 리턴
~~~java
import java.util.*;
public class Solution {
    public int[] solution(int[] array, int[][] commands){
        int[] answer = new int[commands.length];
        int idx = 0;
        for(int i=0; i<commands.length; i++){
            int start = commands[i][0];
            int end = commands[i][1];
            int k = commands[i][2];
            int l=0;
            int[] subArray = new int[end-start+1];
            for(int j=start-1; j<end; j++){
                subArray[l++] = array[j];
                            }
            Arrays.sort(subArray);
            answer[idx++]=subArray[k-1];
        }
        return answer;
    }
}
~~~

### 풀이 2
Arrays.copyOfRange 이용했습니다.
~~~java
import java.util.*;
public class Solution {
    public int[] solution(int[] array, int[][] commands){
        int [] answer = new int[commands.length];
        int idx = 0;
        for(int i=0; i<commands.length; i++){
            int start = commands[i][0];
            int end = commands[i][1];
            int k = commands[i][2];
            int[] subArray = Arrays.copyOfRange(array, start-1, end);
            Arrays.sort(subArray);
            answer[idx++] = subArray[k-1];
        }
        return answer;
    }
}
~~~