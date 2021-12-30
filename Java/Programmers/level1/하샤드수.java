package Java.Programmers.level1;

public class 하샤드수 {
    public static void main(String [] args){
        하샤드수 s = new 하샤드수();
        System.out.println(s.solution(11));
    }
    // 버전 1
    // public boolean solution(int x) {
    //     // String s = Integer.toString(x);
    //     // char [] ch = s.toCharArray();
    //     char [] ch = String.valueOf(x).toCharArray();
    //     int sum = 0;
    //     for (int i=0; i<ch.length; i++){
    //         sum += Integer.parseInt(String.valueOf(ch[i]));
    //     }
    //     if (x%sum==0)
    //         return true;
    //     else
    //         return false;
    // }  

    // 버전 2
    public boolean solution(int x) {
        String [] temp = String.valueOf(x).split("");
        int sum =0;
        for(String s: temp){
            sum += Integer.parseInt(s);
        }
        if(x % sum==0)
            return true;
        else
            return false;
    }
}
