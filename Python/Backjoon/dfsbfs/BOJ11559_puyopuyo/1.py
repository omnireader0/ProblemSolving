from collections import deque
puyo = list(list(map(str, input())) for _ in range(12))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y): 
    q = deque()
    q.append((x, y))
    temp = []
    while q:
        x, y = q.popleft()
        if not (x, y) in temp:
            temp.append((x, y))
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < 12 and 0 <= ny < 6 and puyo[x][y] == puyo[nx][ny] :
                    q.append((nx, ny))
    return temp

def drop():
    for i in range(11, -1, -1):
        for j in range(6):
            if puyo[i][j] == '.':
                for k in range(i-1, -1, -1):
                    if puyo[k][j] != '.':
                        puyo[i][j], puyo[k][j] = puyo[k][j], '.'
                        break

answer = 0
while True:
    flag = 0
    for i in range(12):
        for j in range(6):
            if puyo[i][j] != '.':
                result = bfs(i, j)
                if len(result) >= 4:
                    if flag == 0:
                        flag = 1
                    for a, b in result:
                        puyo[a][b] = '.'
                        
    drop()
    if flag == 1:
        answer += 1
    else:
        break
print(answer)

'''
R, G, B, P, Y

각 뿌요에 대해 뿌요를 만나면 bfs 돌린다.
뿌요 터뜨리고, 뿌요를 아래로 떨어뜨린다.
이것을 터질 뿌요 있을 때까지 반복한다

'''