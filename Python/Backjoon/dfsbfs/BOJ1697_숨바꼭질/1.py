from collections import deque

n, k = map(int, input().split())
graph = [0]*100001

def bfs():
    q = deque()
    q.append(n)
    while q:
        v = q.popleft()
        
        if v == k:
            return graph[v]
        
        for next in (v-1, v+1, v*2):
            if 0 <= next < 100001 and graph[next] == 0:
                graph[next] = graph[v] + 1
                q.append(next)
print(bfs())