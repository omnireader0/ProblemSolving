package Java.Programmers.level3.네트워크.solution1;

class Solution {
    static int[] visited;

    public void dfs(int[][] computers, int v) {
        visited[v] = 1;
        for (int i=0; i<computers.length; i++){
            if (computers[v][i] == 1 && visited[i] == 0) {
                dfs(computers, i);
            }
        }
    }
    public int solution(int n, int[][] computers) {
        int answer = 0;
        visited = new int[n];
        for (int i=0; i<n; i++) {
            if (visited[i] == 0) {
                dfs(computers, i);
                answer++;
            }
        }
        return answer;
    }
}