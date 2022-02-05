package Java.Programmers.level1.하샤드수.solution3;

class Solution {
    public boolean solution(int x) {
        int s = sumDigits(x);
        return x % s == 0;
    }
    public int sumDigits(int x) {
        int sum = 0;
        while(x > 0){
            sum += x % 10;
            x /= 10;
        }
        return sum;
    }
}
