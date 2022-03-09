n, l, r= map(int, input().split())
map = list(list(map(int, input().split())) for _ in range(n))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] 
cnt = 0
united = {}

def dfs(i, j, idx):
    visited[i][j] = idx
    if idx not in united:
        united[idx] = [map[i][j], 1]
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < n and 0 <= ny < n and (l <= abs(map[i][j] - map[nx][ny]) <= r) and visited[nx][ny]==0:
            united[idx][0] += map[nx][ny]
            united[idx][1] += 1
            dfs(nx, ny, idx)
    

while True:
    idx = 1
    united = {}
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0:
                dfs(i,j,idx)
                idx += 1
    
    for i in range(n):
        for j in range(n):
            map[i][j] = united[visited[i][j]][0] // united[visited[i][j]][1]
    
    if len(united)== n*n:
        break
    cnt += 1
print(cnt)