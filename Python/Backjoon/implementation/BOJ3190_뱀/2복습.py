# import sys
# input = sys.stdin.readline

# delta = {'R': [0,1], 'L': [0,-1], 'U': [-1,0], 'D': [1,0]}
# directions = ['R', 'D', 'L', 'U'] # 동 남 서 북

# N = int(input()) # 보드의 크기
# K = int(input()) # 사과의 갯수

# board = [[0]*N for _ in range(N)] 
# board[0][0] = 'R' 

# # 사과 위치 
# for _ in range(K):
#     r, c = map(int, input().split())
#     board[r-1][c-1] = 1

# # 이동 순서 입력 
# M = int(input())
# moves = {}
# for _ in range(M):
#     x, c = input().split()
#     moves[x] = c

# hr, hc = 0, 0 # 머리(head) 인덱스
# tr, tc = 0, 0 # 꼬리(tail) 인덱스
# hd = 0 # 머리의 진행 방향
# time = 0
# flag = False # 사과를 먹었는지 유무

# while True:

#     time += 1

#     # 1. 머리가 한칸 이동
#     dr, dc = delta[directions[hd]]
#     hr, hc = hr+dr, hc+dc

#     # 2. 벽 또는 자기 자신과 부딪혔는지 체크
#     if (hr < 0) or (hc < 0) or (hr >= N) or (hc >= N):
#         break
#     elif str(board[hr][hc]).isalpha():
#         break
    
#     # 3. 게임이 끝나지 않았다면 다음 칸으로 이동
#     # 3-1. 방향 전환이 있는지 없는지 확인
#     if str(time) in moves:
#         if moves[str(time)] == 'D':
#             hd = (hd + 1) % 4
#         else:
#             hd = (hd + 3) % 4
    
#     # 3-2. 다음 칸에 사과가 있는지 확인
#     if board[hr][hc]:
#         flag = True 
    
#     # 3-3. 다음 칸으로 이동
#     board[hr][hc] = directions[hd]


#     # 3-4. 사과를 먹지 않았다면, 꼬리도 같이 한칸 앞으로 이동
#     if not flag:
#         dr, dc = delta[board[tr][tc]]
#         board[tr][tc] = 0
#         tr, tc = tr+dr, tc+dc 
    
#     flag = False

# print(time)

import sys
input = sys.stdin.readline

n = int(input())
board = [[False]*n for _ in range(n)]

for _ in range(int(input())):
    i, j = map(int, input().split())
    board[i-1][j-1] = True
    
snake_info = {}
for _ in range(int(input())):
    x, c = input().split()
    snake_info[int(x)] = 1 if c == 'D' else -1

snake = [(0, 0)]
time, direc = 0, 0
dx, dy = [0,1,0,-1], [1,0,-1,0]

while True:
    
    time += 1
    nx, ny = snake[-1][0] + dx[direc], snake[-1][1] + dy[direc]
    
    if not (0 <= nx < n and 0 <= ny < n) or (nx, ny) in snake:
        break
    
    if board[nx][ny]:   # 사과 O
        board[nx][ny] = False
        
    else:
        snake.pop(0)
    snake.append((nx, ny))
    
    if time in snake_info:
        direc = (direc + snake_info[time]) % 4
        snake_info.pop(time)
print(time)