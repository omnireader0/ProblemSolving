package Java.Programmers.level2.게임맵최단거리.solution2;

import java.util.*;
class Solution {
    
    static final int dx[] = {-1, 1, 0, 0};
    static final int dy[] = {0, 0, -1, 1};
    
    class Node {
        private int x;
        private int y;
        
        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
        public int getX() {
            return this.x;
        }
        public int getY() {
            return this.y;
        }
    }
    
    public int solution(int[][] maps) {
        final int n = maps.length-1;
        final int m = maps[0].length-1;
        int answer = Integer.MAX_VALUE;
        boolean[][] visited = new boolean[n+1][m+1];
        int[][] d = new int[n+1][m+1];
        
        Queue<Node> q = new LinkedList<>();
        q.offer(new Node(0, 0));
        visited[0][0] = true;
        d[0][0] = 1;
        
        while(!q.isEmpty()) {
            Node node = q.poll();
            
            int x = node.getX();
            int y = node.getY();
            int distance = d[x][y];
            
            if (x == n && y == m) {
                answer = Math.min(distance, answer);
                break;
            }
            
            for(int i=0; i<4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (nx < 0 || nx > n || ny < 0 || ny > m) continue;
                
                if (maps[nx][ny] == 0) continue;
                
                if (visited[nx][ny]) continue;
                
                d[nx][ny] = distance + 1;
                visited[nx][ny] = true;
                q.offer(new Node(nx, ny));
                
            }
        }
        return answer == Integer.MAX_VALUE ? -1 : answer;
    }
}