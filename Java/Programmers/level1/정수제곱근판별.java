package Java.Programmers.level1;

public class 정수제곱근판별 {
    

    public static void main(String [] args){
        정수제곱근판별 s = new 정수제곱근판별();
        System.out.println(s.solution(121));
    }
    
    // double answer = Math.sqrt(n);
    // if (answer*answer != n)
    //     return -1;
    // else 
    //     return ((long)answer+1)*((long)answer+1);
    public long solution(long n){
        long answer = 0;
        for(long i=0; i*i<=n; i++){
            if (i*i==n){
                answer = (i+1)*(i+1);
            }
            else
                answer = -1;
        }
        return answer;    
    }
}
