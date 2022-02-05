import java.util.*;
public class Solution {
    public int solution(String begin, String target, String[] words) {
        int answer = bfs(begin, target, words);
        return answer;
    }

    class Node {
        String word;
        int cnt;

        public Node(String word, int cnt) {
            this.word = word;
            this.cnt = cnt;
        }
    }

    private int countDifference(String w1, String w2) {
        int cnt = 0;
        for (int i = 0; i<w1.length(); i++) {
            if(w1.charAt(i) != w2.charAt(i)) cnt++;
        }
        return cnt;
    }

    private int bfs(String begin, String target, String[] words) {
        Queue<Node> q = new LinkedList<>();
        int[] visited = new int[words.length];

        q.add(new Node(begin, 0));

        while(!q.isEmpty()) {
            
            Node n = q.poll();
            String word = n.word;
            int cnt = n.cnt;

            if(word.equals(target)) return cnt;

            for(int i=0; i<words.length; i++) {
                if (visited[i] == 0 && countDifference(word, words[i]) == 1) {
                    visited[i] = 1;
                    q.add(new Node(words[i], cnt+1));
                }
            }
        }
        return 0;
    }
}