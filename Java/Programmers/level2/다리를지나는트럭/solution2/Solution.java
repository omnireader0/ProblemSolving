package Java.Programmers.level2.다리를지나는트럭.solution2;

import java.util.LinkedList;
import java.util.Queue;
import java.util.ArrayList;
import java.util.List;
class Solution {

    class Truck {
        private int remainDistance;
        private int weight;

        public Truck(int remainDistance, int weight) {
            this.remainDistance = remainDistance;
            this.weight = weight;
        } 

        public boolean isFinished() {
            return remainDistance == 0;
        }

        public void move() {
            remainDistance--;
        }
        public int getWeight() {
            return weight;
        }
    }

    class Bridge {
        private int length;
        private int maxWeight;
        private List<Truck> trucks = new ArrayList<>();
        private int currentWeight = 0;

        public Bridge(int length, int maxWeight) { 
            this.length = length;
            this.maxWeight = maxWeight;
        }

        public List<Truck> getTrucks() {
            return trucks;
        }

        public boolean isTruckWeightAvailable(Truck truck) {
            return currentWeight + truck.getWeight() <= maxWeight;
        }

        public void enterTruck(Truck truck) {
            currentWeight += truck.getWeight();
            trucks.add(truck);
            truck.move();
        }

        public void moveTrucks() {
            for (int i = 0; i<trucks.size(); i++) {
                trucks.get(i).move();
            }
        }

        public int getLength() {
            return length;
        }

        public void setLength(int length) {
            this.length = length;
        }

        public void removeIfArrived() {
            if (trucks.get(0).isFinished()) {
                currentWeight -= trucks.get(0).getWeight();
                trucks.remove(0);
            }
        }   
    }
   
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        Bridge bridge = new Bridge(bridge_length, weight);
        Queue<Truck> waiting_trucks = new LinkedList<>();
        for (int w : truck_weights) {
            waiting_trucks.offer(new Truck(bridge_length, w));
        }
        
        while (!waiting_trucks.isEmpty() || bridge.getTrucks().size() > 0) {
            Truck truck = waiting_trucks.peek();
            if(truck == null) { // 대기 트럭이 없다면 다리 위 트럭 처리
                bridge.removeIfArrived();
                bridge.moveTrucks();
                answer++;
                continue;
            }
            bridge.moveTrucks();
            if (bridge.isTruckWeightAvailable(truck)) {
                waiting_trucks.poll();
                bridge.enterTruck(truck);
            }
            bridge.removeIfArrived();
            answer++;
        }
        return answer;
    }
}