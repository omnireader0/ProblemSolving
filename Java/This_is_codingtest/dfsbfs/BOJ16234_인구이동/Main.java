package Java.This_is_codingtest.dfsbfs.BOJ16234_인구이동;
import java.util.*;

class Position {
    private int x;
    private int y;
    
    public Position(int x, int y) {
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
public class Main {
    
    public static int n,l,r;
    public static int cnt = 0;

    public static int[][] map = new int[50][50];
    public static int[][] visited = new int[50][50];

    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};

    public static void bfs(int x, int y, int idx) {

        // 위치와 연결된 나라 정보를 담는 리스트
        ArrayList<Position> united = new ArrayList<>();
        united.add(new Position(x,y));

        // bfs 
        Queue<Position> q = new LinkedList<>();
        q.offer(new Position(x,y));
        visited[x][y] = idx;
        int now = map[x][y]; // 현 연합의 전체 인구 수
        int count = 1; // 현재 연합 국가 수

        while (!q.isEmpty()) {
            
            Position pos = q.poll();
            
            x = pos.getX();
            y = pos.getY();

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (0 <= nx && nx < n  && 0 <= ny && ny < n && visited[nx][ny] == -1) {
                    int gap = Math.abs(map[nx][ny]- map[x][y]);
                    if (l <= gap && gap <= r) {
                        q.offer(new Position(nx, ny));

                        visited[nx][ny] = idx;
                        now += map[nx][ny];
                        count += 1;
                        united.add(new Position(nx, ny));
                    }
                }
            }
        }
        // 인구 이동
        for (int i = 0; i < united.size(); i++) {
            x = united.get(i).getX();
            y = united.get(i).getY();
            map[x][y] = now / count;
        }
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        l = sc.nextInt();
        r = sc.nextInt();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                map[i][j] = sc.nextInt();
            }
        }

        while (true) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    visited[i][j] = -1;
                }
            }
            int idx = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (visited[i][j] == -1) {
                        bfs(i, j, idx);
                        idx += 1;
                    }
                }
            } 
            if (idx == n*n) break;
            cnt += 1;
        }

        System.out.println(cnt);
    }
}

/** 
 
 united : 연합 나라의 정보를 담는 리스트
 

 연합 가능한 나라를 찾고, 인구이동을 하는 bfs 구현
로직은 파이썬에서와 비슷, 다만 dfs가 아니라 bfs를 적용
*/


