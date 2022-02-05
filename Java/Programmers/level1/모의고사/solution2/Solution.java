package Java.Programmers.level1.모의고사.solution2;

import java.util.*;
class Solution {
    
    class Student {
        private int[] answers;
        private int cnt;
        private int id = 0;
        
        public Student(int id, int[] answers) {
            this.answers = answers;
            this.cnt = 0;
            this.id = id;
        }
        
        public void matchAnswer(int[] matchAnswers) {
            for (int i=0; i<matchAnswers.length; i++) {
                if (matchAnswers[i] == answers[i % answers.length])
                    cnt++;
            }
        }
        
        public int getId() {
            return id;
        }
        
        public int getCnt() {
            return cnt;
        }
        
    }
    
    public int[] solution(int[] answers) {
        
        Student[] students = {
            new Student(1, new int[]{1, 2, 3, 4, 5}),
            new Student(2, new int[]{2, 1, 2, 3, 2, 4, 2, 5}),
            new Student(3, new int[]{3, 3, 1, 1, 2, 2, 4, 4, 5, 5})
        };

        int max = Integer.MIN_VALUE;
        
        for (int i=0; i<students.length; i++) {
            students[i].matchAnswer(answers);
            max = Math.max(max, students[i].getCnt());
        }
        
        ArrayList<Integer> list = new ArrayList<Integer>();
        
        for (int i=0; i<students.length; i++) {
            if (students[i].getCnt() == max)
                list.add(students[i].getId());
        }

        return list.stream().mapToInt(i->i).toArray();
    }
}