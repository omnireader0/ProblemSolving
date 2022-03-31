n, m, r = map(int, input().split())
graph = list(list(map(int, input().split()))for _ in range(n))

def rotate():
    cnt = min(n,m)//2 # 테두리 개수
    for i in range(cnt):
        nn = n-i-1
        mm = m-i-1
        start = graph[i][i]
        # 위 : 왼 <- 오
        for j in range(i, mm):
            graph[i][j] = graph[i][j+1]
        # 오른쪽 : 위 <- 아래
        for j in range(i, nn):
            graph[j][mm] = graph[j+1][mm]
        # 아래 : 오 <- 왼
        for j in range(mm, i, -1):
            graph[nn][j] = graph[nn][j-1]
        # 왼쪽 : 아래 <- 위
        for j in range(nn, i, -1):
            graph[j][i] = graph[j-1][i]
        graph[i+1][i] = start

if r > 2*(n+m)-4:
    r = r%(2*(n+m)-4)
for i in range(r):
    rotate()
for i in graph:
        for j in i:
            print(j, end=' ')
        print()
   
    