package Java.Programmers.level1;

public class 짝수와홀수 {
    public static void main(String [] args){
        짝수와홀수 s = new 짝수와홀수();
        System.out.println(s.solution(3));
    }
    public String solution(int num){
        String answer = "Odd";
        if (num%2 != 0)
            return answer;
        else
            return "Even";
    }
}
