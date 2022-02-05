package Java.Programmers.level2.다리를지나는트럭.solution1;

/*
bridge 길이만큼 크기를 갖고 있고, 이 크기 유지
bridge가 비어있지 않다면, 맨앞 원소 pop, 조건에 맞게 수행
bridge 비어있다면, 대기 트럭은 비어있을 것
*/
import java.util.LinkedList;
import java.util.Queue;
class Solution {
   
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int time = 0;
        Queue<Integer> waiting_trucks = new LinkedList<>(); // 대기하고 있는 트럭
        Queue<Integer> bridge = new LinkedList<>(); // 다리 위 트럭
        
        for (int i : truck_weights) {
            waiting_trucks.offer(i);
        } 

        for (int i=0; i<bridge_length; i++){
            bridge.offer(0);
        }

        while(!bridge.isEmpty()) {
            bridge.poll();
            time++;
            int sum_bridge = 0; // 다리 위 트럭들의 무게
            if (!waiting_trucks.isEmpty()) {
                for(int i: bridge) {
                    sum_bridge += i;
                 }
                 if ((sum_bridge + waiting_trucks.peek()) <= weight) {
                     bridge.offer(waiting_trucks.poll());
                 }
                 else
                    bridge.offer(0); 
            }
        }
        return time;
    }
}