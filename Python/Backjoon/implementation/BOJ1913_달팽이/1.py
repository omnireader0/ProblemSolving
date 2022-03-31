n = int(input())
target = int(input())
snail = [[0]*n for _ in range(n)]
start = n*n

# 하 우 상 좌
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x , y = 0, 0
direction = 0
while True:
    if start == 0:
        break
    
    snail[x][y] = start
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    if nx >= n or nx < -1 or ny >= n or ny < -1 or snail[nx][ny] != 0:
        if direction == 3:
            direction = 0
        else:
            direction = direction + 1
    
    x = x + dx[direction]
    y = y + dy[direction]
    start = start -1
    
for i in range(n):
    if target in snail[i]:
        tx = i+1
        ty = snail[i].index(target) + 1
    for j in range(n):
        print(snail[i][j], end=' ')
    print()
print(tx, ty)