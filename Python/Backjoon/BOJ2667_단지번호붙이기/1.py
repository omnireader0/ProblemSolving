n = int(input())
graph = list(list(map(int, input())) for _ in range(n))
answer = []
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def dfs(x, y):
    global cnt
    graph[x][y] = 2
    
    for k in range(4):    
        nx = x + dx[k]
        ny = y + dy[k]
        
        if 0 <= nx <n and 0 <= ny <n and graph[nx][ny] == 1:
            cnt += 1
            dfs(nx, ny)
              
cnt = 1
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i,j)
            answer.append(cnt)
            cnt = 1

print(len(answer))
for i in sorted(answer):
    print(i)