import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] answer = {};
        Queue<Integer> q = new LinkedList<>();
        ArrayList<Integer> result = new ArrayList<>();

        for (int i = 0; i<progresses.length; i++) {
            q.offer((int)Math.ceil((double)(100- progresses[i]) / speeds[i]));
        }
        int prev = q.peek();
        int cnt = 0;

        while (!q.isEmpty()) {
            int now = q.poll();

            if (now <= prev) {
                cnt++;
                continue;
            }
            result.add(cnt);
            prev = now;
            cnt = 1;
        }
        result.add(cnt);
        answer = result.stream().mapToInt(i->i).toArray();
        return answer;
    }
}