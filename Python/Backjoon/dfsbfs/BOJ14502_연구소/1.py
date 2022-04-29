'''
0 빈 칸
1 벽
2 바이러스
'''
from itertools import combinations
from copy import deepcopy
n,m = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(n))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, copy_graph):
    copy_graph[x][y] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m:
            if copy_graph[nx][ny] == 0:
                dfs(nx, ny, copy_graph)  

empty = []
virus = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty.append((i,j))    

combi = list(combinations(empty, 3))
answer = 0

for co in combi:
    result = 0
    copy_graph = deepcopy(graph)
    
    for c in co:
        i, j = c[0], c[1]
        copy_graph[i][j] = 1

    for i in range(n):
        for j in range(m):
            if copy_graph[i][j] == 2:
                dfs(i, j, copy_graph)
    
    for i in copy_graph:
        result += i.count(0)
        
    answer = max(answer, result)
print(answer)