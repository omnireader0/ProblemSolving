from collections import deque
import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(v):
    q = deque()
    q.append(v)
    while q:
        t = q.popleft()
        for i in graph[t]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)