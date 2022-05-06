'''
최단 경로에 가중치가 있으므로 다익스트라로 해결한다.
다익스트라는 보통 힙을 사용하여 우선순위 높은 원소를 먼저 삭제한다.

다익스트라의 시간복잡도는 o(v+e)
문제에서 간선 개수 십만, 노드 개수 만개이므로 1초안에 문제를 해결할 수 있다.
'''
import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)
n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
for _ in range(m):
    a, b, c = map(int , input().split())
    graph[a].append((b, c))
    
d, e = map(int, input().split())

def dijkstra(d):
    q = []
    heapq.heappush(q, (0, d)) # 비용, 노드
    distance[d] = 0
    
    while q:
        dist, now = heapq.heappop(q) # 최단 거리 가장 짧은 노드 꺼내기
        if distance[now] < dist:
            continue
        # 현재 노드와 인접 노드 확인
        for i in graph[now]:
            cost = dist + i[1] # 현재 노드를 거쳐간 비용
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
    
dijkstra(d)
print(distance[e])