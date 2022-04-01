import sys
input = sys.stdin.readline
board = list(list(map(int, input().split())) for _ in range(19))
# 오른 위 대각선, 오른쪽, 오른 아래 대각선, 아래
dx = [-1, 0, 1, 1]
dy = [1, 1, 1, 0]

def rotate(i,j):
    t = board[i][j]
    for d in range(4):
        cnt = 1
        x = i
        y = j
        while True:
            x += dx[d]
            y += dy[d]
            if (x < 0 or y < 0 or x >= 19 or y >= 19) or board[x][y] != t:
                break
            cnt += 1
        if cnt == 5:
            x = i-dx[d]
            y = j-dy[d]
            if x < 0 or y < 0 or x >= 19 or y >= 19 or board[x][y] != t:
                return t
    return 0
result = 0
for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            result = rotate(i,j)
            if result != 0:
                break      
    if result != 0:
        break
print(result)
if result != 0:
    print(i+1, j+1)
'''
스타트를 한 바둑알 저장
while문을 통해 조건 만족하면 cnt 갱신
cnt가 5개인 경우 처음 바둑알의 반대 방향에 위치한 바둑알이 같은 색상인지 체크
'''