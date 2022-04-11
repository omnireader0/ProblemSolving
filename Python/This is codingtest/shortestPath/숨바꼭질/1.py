import heapq
import sys
input = sys.stdin.readline
n,m = map(int, input().split()) 
array = [[] for _ in range(n+1)] # 노드에 연결된 노드에 대한 정보 담기
distance = [1e9] * (n+1)
start = 1

for _ in range(m):
    a, b = map(int, input().split()) 
    array[a].append((b, 1))
    array[b].append((a, 1))

q = []
heapq.heappush(q, (0, start)) # 시작 노드로 가는 최소비용 0
distance[start] = 0

while q:
    dist, now = heapq.heappop(q)
    
    if distance[now] < dist:
        continue
    
    for i in array[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

result = list(map(lambda x: -1 if x >= 1e9 else x, distance))
length = max(result)

print(result.index(length), length, result.count(length))