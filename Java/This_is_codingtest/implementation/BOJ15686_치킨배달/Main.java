package Java.This_is_codingtest.implementation.BOJ15686_치킨배달;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int n, m, answer;
    static int[][] map;
    static ArrayList<int[]> chickens, home;
    public static void main(String[] args) throws Exception{
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(in.readLine().trim());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        chickens = new ArrayList<int[]>();
        home = new ArrayList<int[]>();
        map = new int[n][n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(in.readLine().trim());
            for (int j = 0; j < n; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if (map[i][j] == 2) {
                    chickens.add(new int[] {i,j});
                }else if (map[i][j] == 1) {
                    home.add(new int[] {i,j});
                }
            }
        }
        answer = Integer.MAX_VALUE;
        getDistance(0, 0, new ArrayList<String>());
        System.out.println(answer);
    }

    private static void getDistance(int cnt, int start, ArrayList<String> list) {
        if (cnt==m) {
            int dist = 0;
            for (int[] h: home) {
                int min = Integer.MAX_VALUE;
                for (String i : list) {
                    int[] ch = chickens.get(Integer.parseInt(i));
                    min = Math.min(min, Math.abs(ch[0]-h[0])+Math.abs(ch[1]-h[1]));
                }
                dist += min;
            }
            answer = Math.min(answer, dist);
            return;
        }
        // 백트래킹
        for (int i=0; i<chickens.size(); i++) {
            list.add((i) + "");
            getDistance(cnt+1, i+1, list);
            list.remove((i) + "");
        }
    }

    

}



// 1. 치킨집, 집의 위치 담기
// 2. 치킨집 m개 조합 구하기 - 그 조합에 따른 치킨 거리 최솟값 구하기
// 3. 치킨 거리 최솟값 구하는 함수를 만들자

// 자바로 이차 배열 입력 받는법
// 밥먹구 와서 이어서 하기

//Cannot make a static reference to the non-static method getDistance(int, int, ArrayList<String>) from the type MainJava(603979977)

