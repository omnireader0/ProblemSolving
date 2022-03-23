'''
벽 1
뱀 2
사과 3
'''
n = int(input())
board = [[1]*(n+2)] + [[1] + [0]*n + [1] for _ in range(n)] + [[1]*(n+2)]

# 사과
apple = int(input())
for _ in range(apple):
    i, j = map(int, input().split())
    board[i][j] = 3
    
# 방향 정보
data = []
di = int(input())
for _ in range(di):
    t, d = map(str, input().split())
    data.append((int(t), d))
    
# 동 남 서 북, direction : 0 1 2 3 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, d):
    if d == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction
x, y = 1, 1
board[x][y] = 2
direction = 0
time = 0
next_turn = 0 # 회전 수
q = [(x, y)]

while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    if 1<= nx <= n and 1 <= ny <= n and board[nx][ny] != 2:
        # 사과 있다면 사과 제거 + 꼬리 유지
        if board[nx][ny] == 3:
            board[nx][ny] = 2
            q.append((nx, ny))
        if board[nx][ny] == 0:
            board[nx][ny] = 2
            q.append((nx, ny))
            tx, ty = q.pop(0)
            board[tx][ty] = 0
            
    else:
        time += 1
        break
    
    x, y = nx, ny
    time += 1
    if next_turn <di and time == data[next_turn][0]:
        direction = turn(direction, data[next_turn][1])
        next_turn += 1
print(time)
            
'''
풀이

뱀의 이동 정보는 큐에 담기
사과, 뱀, 벽의 값을 다 다르게 줌
방향 전환 함수 잘 설계
'''