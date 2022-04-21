from collections import deque

n = int(input())
graph = list(list(map(int, input().split())) for _ in range(n))

# 위 왼 아 오
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
    
size = 2
nx, ny = 0, 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            nx, ny = i, j
            graph[nx][ny] = 0
                
# 최단거리
def bfs():

    distance = [[-1] * n for _ in range(n)]
    q = deque([(nx, ny)])
    distance[nx][ny] = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx_ = x + dx[i]
            ny_ = y + dy[i]
            if 0 <= nx_ < n and 0 <= ny_ < n:
                if distance[nx_][ny_] == -1 and graph[nx_][ny_] <= size:
                    distance[nx_][ny_] = distance[x][y] + 1
                    q.append((nx_, ny_))
                    
    return distance

# 먹을 물고기 찾기
def find(distance):
    x, y = 0, 0
    min_ = int(1e9)
    for i in range(n):
        for j in range(n):
            if distance[i][j] != -1 and 1 <= graph[i][j] < size:
                if distance[i][j] < min_: # 가까운 한 마리 먹기
                    x, y = i, j
                    min_ = distance[i][j]
    if min_ == int(1e9):
        return None
    else:
        return x, y, min_
    
result = 0
ate = 0

while True:
    value = find(bfs())
    if value == None:
        print(result)
        break
    else:
        nx, ny = value[0], value[1]
        result += value[2]
        # 먹은 위치 물고기 치우기
        graph[nx][ny] = 0
        ate += 1
        # 현재 자신 크기 이상으로 먹은 경우, 크기 증가
        if ate >= size:
            size += 1
            ate = 0
        
    
'''
1. 최단 거리 : 먹을 수 있는 물고기 중 가장 가까운 물고기를 먼저 먹는다.
2. 자신의 크기보다 작은 물고기만 먹을 수 있다.+

'''