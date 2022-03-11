from collections import deque
n,m,v = map(int, input().split())
graph =[[0]*(n+1) for i in range(n+1)] # 인접 행렬
for i in range(m):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1 

visited1 = [0]*(n+1)
visited2 = [0]*(n+1)

def dfs(v):
    visited1[v] = 1 
    print(v, end=' ')
    
    for i in range(1, n+1):
         if not visited1[i] and graph[v][i]==1:
            dfs(i)

def bfs(v):
    q = deque()
    q.append(v)
    visited2[v] = 1
    
    while q:
        v = q.popleft()
        print(v, end=' ')
        
        for i in range(1, n+1):
            if not visited2[i] and graph[v][i]==1:
                q.append(i)
                visited2[i] = 1

dfs(v)
print()
bfs(v)

