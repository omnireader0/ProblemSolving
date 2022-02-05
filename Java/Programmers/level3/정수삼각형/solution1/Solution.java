package Java.Programmers.level3.정수삼각형.solution1;

class Solution {
    public int solution(int[][] triangle) {
        for (int i = triangle.length-1; i >= 0; i--) {
            for (int j = 0; j < i; j++) {
                triangle[i-1][j] += Math.max(triangle[i][j], triangle[i][j+1]);
            } 
        }
        return triangle[0][0];
    }
}