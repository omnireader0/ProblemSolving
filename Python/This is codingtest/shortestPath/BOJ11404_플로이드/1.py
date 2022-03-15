import sys
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)] 
# 자기 자신으로 가는 비용 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
            
# 정보 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c

# 플로이드 워셜
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][k] + graph[k][b], graph[a][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')
    print()

'''
플로이드 워셜로 해결
그 이유는 모든 도시 쌍에 대해 최소 거리 구하기
'''