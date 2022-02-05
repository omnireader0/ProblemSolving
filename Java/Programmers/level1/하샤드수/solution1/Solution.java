class Solution {
    public boolean solution(int x) {
        char [] ch = String.valueOf(x).toCharArray();
        int sum = 0;
        for(int i = 0; i < ch.length; i++){
            sum += Integer.parseInt(String.valueOf(ch[i]));
        }
        return x%sum == 0;
    }
}