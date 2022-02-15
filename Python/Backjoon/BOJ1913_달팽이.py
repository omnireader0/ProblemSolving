'''
n*n 크기의 그래프를 생성하고 0으로 초기화
아래 0 오른 1 위 2 왼 3 모양의 dx, dy 생성
처음 start_num 은 n*n
while문에서 start_num이 0이 될때까지 그래프 채워나가기 
그래프 채워나가는 법
- 그래프에 값 넣고, 다음 방문할 곳 모색한다. x, y를 다음 방문할 좌표로 변경
- 이때, 방문할 수 없는 곳이라면, 방향 바꿔주기 
- start_num -= 1 
'''
n = int(input())
target = int(input())
graph = [[0]*n for _ in range(n)]
start_num = n*n

# 하 우 상 좌
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
x = 0
y = 0
direction = 0 

while True:
    if start_num == 0:
        break
    
    graph[x][y] = start_num
    nx = x + dx[direction]
    ny = y + dy[direction]
    if nx <= -1 or nx >= n or  ny <= -1 or ny >= n or graph[nx][ny] != 0:
        if direction == 3:
            direction = 0
        else:
            direction += 1
    x = x + dx[direction]
    y = y + dy[direction]
    start_num -= 1
    
for i in range(n):
    if target in graph[i]:
        kx = i
        ky = graph[i].index(target)
    for j in range(n):
        print(graph[i][j], end=' ')
    print()
print(kx+1, ky+1)
    
