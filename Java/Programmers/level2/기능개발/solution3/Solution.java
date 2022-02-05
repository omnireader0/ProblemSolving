import java.util.*;

class Solution {

    private class Task {
        private int progresses;
        private int speeds;

        public Task(int progresses, int speeds) {
            this.progresses = progresses;
            this.speeds = speeds;
        }

        public void process() {
            progresses += speeds;
        }

        public boolean isCompleted() {
            return progresses >= 100;
        }
    }

    public int[] solution(int[] progresses, int[] speeds) {

        int[] answer = {};

        Queue<Task> q = new LinkedList<>();
        for (int i=0; i<progresses.length; i++) {
            q.add(new Task(progresses[i], speeds[i]));
        }

        List<Integer> result = new ArrayList<>();
        
        while (!q.isEmpty()) {
            for (Task t : q) {
                t.process();
            }

            int cnt = 0;
            while(!q.isEmpty() && q.peek().isCompleted()) {
                q.poll();
                cnt++;
            }
            
            if (cnt > 0){
                result.add(cnt);
            }
        }

        answer = result.stream().mapToInt(a->a).toArray();
        return answer;
    }
}