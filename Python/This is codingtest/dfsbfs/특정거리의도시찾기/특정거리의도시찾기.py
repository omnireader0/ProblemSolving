'''
도시 n 도로 m 거리 k 출발 도시의 번호 x
최단거리 + 간선의 비용이 동일 -> bfs
bfs의 시간복잡도 o(n+m) -> 그래프를 인접리스트로 표현한다면

출발 도시로부터 bfs 수행하여, 모든 도시까지의 최단 거리를 구하고
최단거리가 k인 모든 도시 출력하자!!

채점 시 python의 경우 -> import sys 후 sys.stdin.readline().rstrip().split()으로 입력해야 통과
거리 개수 최대가 백만개인데, 여기서 입력받을 때 시간 초과 발생

채점 시 pypy로 하면 그냥 통과
'''
from collections import deque
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    
distance = [-1] * (n+1)
distance[x] = 0

q = deque()
q.append(x)

while q:
    now = q.popleft()
    for next in graph[now]:
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            q.append(next)
        
flag = False
for i in range(1, n+1):
    if distance[i] == k:
         print(i)   
         flag = True

if not flag:
    print(-1)