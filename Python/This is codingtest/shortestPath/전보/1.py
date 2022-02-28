import heapq
import sys

input = sys.stdin.readline

n,m,start = map(int, input().split()) # 도시 개수, 통로 개수, 출발 도시
array = [[] for _ in range(n+1)] # 노드에 연결된 노드에 대한 정보 담기
distance = [1e9] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split()) # 출발도시, 도착도시, 걸린시간
    array[a].append((b, c))

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

cnt = 0
max_distance = 0
for i in range(1, n+1):
    if distance[i] !=1e9:
        cnt += 1
        max_distance = max(max_distance, distance[i])
print(cnt-1, max_distance)