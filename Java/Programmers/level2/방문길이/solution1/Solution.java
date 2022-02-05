import java.util.*;
class Solution {
    private int[][] direction = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}}; // LRUD
    private HashMap<Character, Integer> map;

    public int solution(String dirs) {
        boolean[][][][] visited = new boolean[11][11][11][11];
        map = new HashMap<>();
        map.put('L', 0);
        map.put('R', 1);
        map.put('U', 2);
        map.put('D', 3);

        int answer = 0;
        int x = 5, y = 5; // 시작 좌표
        for(int i=0; i<dirs.length(); i++){
            int d = map.get(dirs.charAt(i));
            int nx = x+direction[d][0];
            int ny = y+direction[d][1];

            if (nx<0 || nx>10 || ny<0 || ny>10) continue;

            if (!visited[x][y][nx][ny] && !visited[nx][ny][x][y]){
                visited[x][y][nx][ny] = true;
                visited[nx][ny][x][y] = true;
                answer++;
            }
            x=nx;
            y=ny;
        }
        return answer;
    }
}