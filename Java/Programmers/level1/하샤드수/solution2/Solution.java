package Java.Programmers.level1.하샤드수.solution2;

// sol2 : 합 구할 때 char -> int 형변환
class Solution {
    public boolean solution(int x) {
        char [] ch = String.valueOf(x).toCharArray();
        int sum = 0;
        for(int i = 0; i < ch.length; i++){
            sum += Character.getNumericValue(ch[i]);
        }
        return x%sum == 0;
    }
}