from collections import deque
n, m, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def rotate(x, y, nn, mm):
    
    q = deque()
    # 왼 -> 오른
    for i in range(y, y+mm):
        q.append(graph[x][i])
    # 위 -> 아래
    for i in range(x+1, x + nn):
        q.append(graph[i][y+mm-1])
    # 오른 -> 왼
    for i in range(y+mm-2, y, -1):
        q.append(graph[x + nn-1][i])
    # 아래 -> 위
    for i in range(x+nn-1, x, -1):
        q.append(graph[i][y])
    q.rotate(-r)

    for i in range(y, y+mm):
        graph[x][i] = q.popleft()
    for i in range(x+1, x+nn):
        graph[i][y+mm-1] = q.popleft()
    for i in range(y+mm-2, y, -1):
        graph[x+nn-1][i] = q.popleft()
    for i in range(x+nn-1, x, -1):
        graph[i][y] = q.popleft()
    
    
nn = n
mm = m
x, y = 0, 0

while True:
    if nn == 0 or mm == 0:
        break
    rotate(x, y, nn, mm)
    x += 1
    y += 1
    nn -= 2
    mm -= 2

for i in graph:
    for j in i:
        print(j, end=" ")
    print()