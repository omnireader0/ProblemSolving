from collections import deque
n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
ts, tx, ty = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
    
data = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))    
   
data.sort()
q = deque(data)

while q:
    v, s, x, y = q.popleft()
    if s == ts:
        break
    for t in range(4):
        nx = x + dx[t]
        ny = y + dy[t]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
            graph[nx][ny] = v
            q.append((graph[nx][ny], s+1, nx, ny))
                
print(graph[tx-1][ty-1])


'''
0이 아닌 노드를 (바이러스, 시간, 위치)에 담고 정렬하여 큐에 넣어서
bfs 처리하면 너무 쉬움
'''