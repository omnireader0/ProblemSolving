import heapq
import sys
input = sys.stdin.readline
INF = 1e9

dx = [-1 ,1 ,0 ,0]
dy = [0, 0, -1, 1]

n = int(input())
for _ in range(n):
    m = int(input())
    graph = list(list(map(int, input().split())) for _ in range(m))
    distance = [[INF]*m for _ in range(m)]
    
    x, y = 0, 0
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]
    
    while q:
        dist, x, y = heapq.heappop(q)
        
        if distance[x][y] < dist:
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny <m :
                cost = dist + graph[nx][ny]
            
                 # 다른 노드 거친 거리가 현재 노드보다 더 짧은 경우    
                if cost < distance[nx][ny] :
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))
    print(distance[m-1][m-1])
    
'''
다익스트라 
bfs
'''