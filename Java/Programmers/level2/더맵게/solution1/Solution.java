package Java.Programmers.level2.더맵게.solution1;

import java.util.PriorityQueue;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0; 
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int a : scoville) {
            pq.offer(a);
        }

        while (pq.size() > 1 && pq.peek() < K) {
            int first = pq.poll();
            int second = pq.poll();
            pq.offer(first+(second*2));
            answer++;
        }

        return pq.peek() >= K ? answer : -1;
    }
}