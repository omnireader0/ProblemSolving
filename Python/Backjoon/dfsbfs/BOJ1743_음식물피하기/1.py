import sys
sys.setrecursionlimit(10000)

n,m,k = map(int, input().split())
graph = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def dfs(x,y):
        visited[x][y] = 1
        global cnt
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny < m and visited[nx][ny] == 0 and graph[nx][ny] ==1:
                dfs(nx, ny)
        

max_cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j]==0:
            cnt = 0
            dfs(i, j)
            max_cnt = max(cnt , max_cnt)
print(max_cnt)
