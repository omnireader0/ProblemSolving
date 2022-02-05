package Java.Programmers.level2.방문길이.solution2;

// sol2 : 방문 표시를 set으로 처리
import java.util.*;
class Solution {
    private int[][] direction = {{0, -1}, {0, 1}, {-1, 0}, {1, 0}}; // LRUD
    private HashMap<Character, Integer> map;

    public int solution(String dirs) {
        Set<String> set = new HashSet<String>(); 
        map = new HashMap<>();
        map.put('L', 0);
        map.put('R', 1);
        map.put('U', 2);
        map.put('D', 3);

        int x = 5, y = 5; // 시작 좌표
        for(int i=0; i<dirs.length(); i++){
            int d = map.get(dirs.charAt(i));
            int nx = x+direction[d][0];
            int ny = y+direction[d][1];

            if (nx<0 || nx>10 || ny<0 || ny>10) continue;
            
            String path1 = x+""+y+""+nx+""+ny;
            String path2 = nx+""+ny+""+x+""+y;
            set.add(path1);
            set.add(path2);
            x=nx;
            y=ny;
        }
        return set.size()/2;
    }
}