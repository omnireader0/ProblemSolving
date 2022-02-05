class Solution {
    
    public void dfs(int[][] computers, int v, int[] visited) {
        visited[v] = 1;
        for (int i=0; i<computers.length; i++){
            if (computers[v][i] == 1 && visited[i] == 0) {
                dfs(computers, i, visited);
            }
        }
    }
    public int solution(int n, int[][] computers) {
        int answer = 0;
        int[] visited = new int[n];
        for (int i=0; i<n; i++) {
            if (visited[i] == 0) {
                dfs(computers, i, visited);
                answer++;
            }
        }
        return answer;
    }
}