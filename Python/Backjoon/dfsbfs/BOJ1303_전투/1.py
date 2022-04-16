m, n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(i, j, cnt):
    color = graph[i][j]
    graph[i][j] = 1
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0<=nx<m  and 0<=ny<n: 
            if graph[nx][ny] == color:
                cnt = dfs(nx, ny, cnt+1)
    return cnt
    
w, b = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'W':
            w += dfs(i, j, 1)**2
        if graph[i][j] == 'B':
            b += dfs(i, j, 1)**2
            
print(w, b)