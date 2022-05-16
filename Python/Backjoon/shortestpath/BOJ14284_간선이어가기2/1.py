'''
다익스트라 적용
무방향 그래프 / 방향 그래프 차이 조심하기
'''
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
start, end = map(int, input().split())
def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q :
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)

print(distance[end])
