from collections import deque
n, m = map(int, input().split())
graph = list(list(map(int, input())) for _ in range(n))
visited = [[0]*m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
x = 0; y = 0
q = deque()
q.append((x, y))
graph[x][y] = 1
visited[x][y] = 1

while q:
    x, y = q.popleft()    
    
    if x == n-1 and y == m-1:
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and visited[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            visited[nx][ny] = 1    
            q.append((nx, ny))
            
print(graph[-1][m-1])

'''
bfs로 해결
이동할 때 마다 전 노드에서 거리 1 증가하여 현 노드에 반영
'''