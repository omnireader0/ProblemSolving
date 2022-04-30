c, r = map(int, input().split()) # 열 행
k = int(input())
graph = [[0]*c for _ in range(r)]

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 0: 상 1: 우 2: 하 3: 좌
direction = 0

x = r-1
y = 0
idx = 1
if c*r < k:
    print(0)
    exit()
else:
    while True:
        if idx == k:
            break
        graph[x][y] = idx
        nx = x + dx[direction]
        ny = y + dy[direction]
        if nx >= r or nx < 0 or ny >= c or ny<0 or graph[nx][ny] !=0:
            if direction == 3:
                direction = 0
            else:
                direction = direction + 1
        x = x + dx[direction]
        y = y + dy[direction]
        idx += 1
    print(y+1, r-x)