INF = int(1e9)
n, m = map(int,input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
            
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][k]+graph[k][b], graph[a][b])
result = 0
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            cnt += 1
    if cnt == n:
        result += 1
print(result)
    
'''
- pypy로 채점
- dfs로 풀어보기

- 플로이드 워셜 풀이
graph[a][b] = 1은 a<b,  키 작은 a가 키 큰b와 키 순서를 비교했음을 표시
반대로
graph[b][a] = 1은 b<a가 된다.

그래서 
graph[a][?] !=INF,  a < ?
graph[?][a] != INF, ? < a
graph[a][a] == 0, 나 자신과의 비교
a가 모든 노드(?)와 비교 가능했다면 모든 사람과 키 순서를 비교했음
'''
    