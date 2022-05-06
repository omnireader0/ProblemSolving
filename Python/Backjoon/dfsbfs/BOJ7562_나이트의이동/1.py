'''
최소 거리를 구하므로 bfs를 적용할 수 있음
체스판의 좌표를 0으로 초기화한후, 그 좌표를 지나가게 되면 값을 갱신해준다.
좌표가 나이트가 이동하려는 좌표와 동일하면 리턴한다. 
'''
from collections import deque
dx = [-1, -2, -2, -1 ,1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    
def bfs(a, b, c, d): 

    q = deque()
    q.append([a, b])
    
    while q:
        x, y = q.popleft()
        
        if x == c and y == d:
            return graph[c][d]
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])
    
t = int(input())
for _ in range(t):
    n = int(input())
    graph = [[0]*n for _ in range(n)]
    
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    graph[a][b] = 1
    answer = bfs(a, b, c, d)
    print(answer-1)