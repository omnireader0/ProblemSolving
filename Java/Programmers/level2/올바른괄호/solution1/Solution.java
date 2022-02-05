package Java.Programmers.level2.올바른괄호.solution1;

class Solution {
    boolean solution(String s) {
        int cnt = 0;
        for(int i=0; i<s.length(); i++){
            if(s.charAt(i)==')' && cnt==0){
                return false;
            }else if(s.charAt(i)==')'){
                cnt--;
            }else if(s.charAt(i)=='('){
                cnt++;
            }
        }
        if(cnt == 0){
            return true;
        }
        return false;
    }
}