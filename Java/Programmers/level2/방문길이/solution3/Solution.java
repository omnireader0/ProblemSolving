import java.util.*;
class Solution {
    
    class Path {
        private Integer x;
        private Integer y;
        private Integer nx;
        private Integer ny;
        
        public Path(Integer x, Integer y, Integer nx, Integer ny) {
            this.x = x;
            this.y = y;
            this.nx = nx;
            this.ny = ny;
        }
        
        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Path path = (Path) o;
            return Objects.equals(x, path.x) && Objects.equals(y, path.y) && Objects.equals(nx, path.nx) && 
            Objects.equals(ny, path.ny) || Objects.equals(x, path.nx) && Objects.equals(y, path.ny) &&
             Objects.equals(nx, path.x) && Objects.equals(ny, path.y);
        }
        
        @Override
        public int hashCode() {
            return Objects.hash(x, y) + Objects.hash(nx, ny);
        }
    }

    public int solution(String dirs) {
        
        int answer = 0;
        Set<Path> set = new HashSet<>(); 
        int[][] direction = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}}; // LRUD
        
        HashMap<Character, Integer> map = new HashMap<>();
        map.put('L', 0);
        map.put('R', 1);
        map.put('U', 2);
        map.put('D', 3);

        int x = 5, y = 5; // 시작 좌표
        for(int i=0; i<dirs.length(); i++){
            int d = map.get(dirs.charAt(i));
            int nx = x+direction[d][0];
            int ny = y+direction[d][1];

            if (nx<0 || nx>10 || ny<0 || ny>10) {
                continue;    
            }
            
            Path path = new Path(x, y, nx, ny);
            
            if(set.add(path)) answer++;
            x = nx;
            y = ny;
        }
        return answer;
    }
}