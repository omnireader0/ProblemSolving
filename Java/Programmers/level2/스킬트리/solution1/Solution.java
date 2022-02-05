package Java.Programmers.level2.스킬트리.solution1;

class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        for(String skills : skill_trees){
            int idx = 0;
            boolean flag = true;
            for(int i=0; i<skills.length(); i++){
                if(skills.charAt(i) == skill.charAt(idx)){
                    idx++;
                    if(idx>=skill.length())
                        break;
                }
                else if(skill.contains(Character.toString(skills.charAt(i))))
                    flag = false;
            }
            if(flag)
                answer++;
        }
        return answer;
    }
}