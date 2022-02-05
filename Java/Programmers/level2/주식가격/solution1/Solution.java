package Java.Programmers.level2.주식가격.solution1;

class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        int size = prices.length;
        for (int i=0; i<size; i++) {
            int cnt = 0;
            for (int j=i+1; j<size; j++){
                cnt++;
                if (prices[i] > prices[j]){
                    break;
                }
            }
            answer[i] = cnt;
        }
        return answer;
    }
}