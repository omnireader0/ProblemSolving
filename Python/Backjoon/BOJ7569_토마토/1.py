from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split()) # 가로 세로 높이
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    q = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 1:
                    q.append([i,j,k])
    
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < h and 0<= ny<n and 0<= nz < m:
                if graph[nx][ny][nz]==0:
                    graph[nx][ny][nz] = graph[x][y][z] + 1
                    q.append([nx, ny, nz])
            
bfs()
            
flag = True
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                print(-1)
                flag = False
                break
        if flag == False:
            break
if flag:
    cnt = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                cnt = max(graph[i][j][k], cnt)
    print(cnt-1)
