package Java.Programmers.level1;

public class 핸드폰번호가리기 {
    public static void main(String [] args){
        핸드폰번호가리기 s = new 핸드폰번호가리기();
        String ph = "01033334444";
        System.out.println(s.solution(ph));
    }
    // 버전 1
    // public String solution(String phone_number){
    //     String answer = "";
    //     for (int i=0; i< phone_number.length()-4; i++){
    //         answer += "*";
    //     }
    //     answer += phone_number.substring(phone_number.length()-4, phone_number.length());
    //     return answer;
    // }

    // 버전 2
    public String solution(String phone_number){
        char [] ch = phone_number.toCharArray();
        for(int i=0; i< ch.length-4; i++){
            ch[i] = '*';
        }
        return String.valueOf(ch);
    }
    // String.valueOf() : 어떤 값을 넣어도 String으로 변환
}
