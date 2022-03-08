package Java.This_is_codingtest.dfsbfs.BOJ14888_연산자끼워넣기;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static int n;
    public static ArrayList<Integer> numbers = new ArrayList<>();
    public static int[] oper = new int[4];
    public static int MAX = (int) -1e9; // 최댓값
    public static int MIN = (int) 1e9; // 최솟값

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();

        for (int i = 0; i < n; i++){
            int x = sc.nextInt();
            numbers.add(x);
        }

        for (int i = 0; i < 4; i++){
            oper[i] = sc.nextInt();
        }

        dfs(numbers.get(0), 1);
        System.out.println(MAX);
        System.out.println(MIN);
    }
    public static void dfs(int num, int idx){
        if (idx == n){
            MAX = Math.max(MAX, num);
            MIN = Math.min(MIN, num);
            return;
        }

        for (int i = 0; i < 4; i++){
            if (oper[i] > 0) {
                oper[i]--;
                switch(i) {
                    case 0 : dfs(num+numbers.get(idx), idx+1); break;
                    case 1 : dfs(num-numbers.get(idx), idx+1); break;
                    case 2 : dfs(num*numbers.get(idx), idx+1); break;
                    case 3 : dfs(num/numbers.get(idx), idx+1); break;
                } 
                oper[i]++;
            }
        }
    }
}