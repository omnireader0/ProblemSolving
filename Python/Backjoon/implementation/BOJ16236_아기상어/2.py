from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
graph = list(list(map(int, input().split())) for _ in range(n))

# 위 왼 아 오
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
    q = deque([(x, y)])
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    feed = []
    while q:
        a, b = q.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # 지나가기만 하는 경우
                if graph[nx][ny] == 0 or graph[nx][ny] == shark:
                    visited[nx][ny] = visited[a][b] + 1
                    q.append((nx, ny))
                # 먹을 수 있는 상어가 있는 경우
                elif 0 < graph[nx][ny] < shark:
                    feed.append((visited[a][b], nx, ny))
                    visited[nx][ny] = visited[a][b] + 1
        
    if feed:
        return sorted(feed)[0]
    else:
        return (-1, -1, -1)
   
        
x, y = 0, 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x, y = i, j
            graph[x][y] = 0
            
shark = 2
answer = 0
ate = 0
while True:
    dist, x, y = bfs(x, y)
    if dist == -1:
        break
    if shark > graph[x][y] :
        ate += 1
        graph[x][y] = 0
    if ate >= shark:
        shark += 1
        ate = 0
    answer += dist
print(answer)

'''
1. 상어가 먹을 수 있는 물고기를 찾아 큐에 담는다.
이때 bfs를 이용해 (상어에서 물고기까지의 거리,  x좌표, y좌표) 큐에 담고,
큐를 sorting해서 맨 앞에 있는 튜플을 리턴한다.(최소 거리)

2. bfs 결과를 받고, 먹은 물고기 수를 세고, 상어의 크기를 결정한다.
먹은 물고기 수 : 상어 크기 보다 작으면 세고, 먹은 물고기 좌표는 0으로 바꾼다.
상어 크기 결정 : 먹은 물고기 수가 상어 크기보다 크면 상어 크기 1 증가하고, 먹은 물고기 수 초기화 

'''