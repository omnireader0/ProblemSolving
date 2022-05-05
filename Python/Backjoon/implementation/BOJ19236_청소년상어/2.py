'''
문제 요약

1. 상어가 (0,0) 물고기 먹고 (0,0) 이동
2. 물고기가 번호 1 ~ 16까지 방향에 맞게 이동
- 이동할 수 있는 칸 : 물고기 있는 칸(상어x), 빈칸
- 이동할 수 있는 칸 있을 때 까지 반시계 45도 회전
- 더 이상 이동할 칸 없으면 끝남
3. 상어 방향에 맞는 칸으로 이동
- 이때, 방향에 맞다면 여러 칸 한번에 이동 가능
- 그리고 그 자리에 있는 물고기 먹고, 물고기 방향 가짐
- 이동 중 지나가는 칸 물고기는 먹지 않음
- 이동 가능한 칸 없다면 집으로 돌아감
4. 다시 2 ~ 3을 반복

물고기 이동 

'''
from copy import deepcopy

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 순서
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

def find(key, arr):
    for x in range(4):
        for y in range(4):
            if arr[x][y] == 's' or arr[x][y] == -1 or key != arr[x][y][0]:
                continue
            return (x, y)
    return (-1, -1)

def rotate(d):
    if d == 8:
        return 1
    else:
        return d + 1

# 물고기 이동
def move(arr):
    global dx, dy
    # 1~16번 물고기 이동
    for i in range(1, 17):
        x, y = find(i, arr)
        if x == -1:
            continue
        
        # 이동 가능할 때까지 8번 방향 전환
        for j in range(8):
            dir = arr[x][y][1]
            nx, ny = x + dx[dir], y + dy[dir]
            
            # 이동할 수 없으면 방향 전환
            if nx < 0 or ny < 0 or nx >= 4 or ny >= 4 or arr[nx][ny] == 's':
                arr[x][y][1] = rotate(dir)
                continue
            
            # 물고기 위치 swap
            tmp = arr[x][y]
            arr[x][y] = arr[nx][ny]
            arr[nx][ny] = tmp
            break
    

def dfs(next, arr_, shark_):
    global answer, dx, dy
    # 백트래킹을 위해 깊은 복사
    arr, shark = deepcopy(arr_), deepcopy(shark_)
    
    # 물고기 잡아먹기
    x, y = shark[1] # 현재 상어의 좌표
    nx, ny = next # 잡아먹을 물고기 좌표
    fish, dir = arr[nx][ny]
    arr[x][y] = -1 # 현좌표 빈칸
    arr[nx][ny] = 's' # 물고기 잡아먹은 위치에 상어 이동
    shark[0] += fish # 잡아먹은 물고기 누적
    shark[1] = (nx, ny) # 잡아먹은 물고기 좌표로 상어 위치 갱신
    shark[2] = dir # 잡아먹은 물고기 방향으로 변경
    x, y = nx, ny # 좌표 이동

    answer = max(shark[0], answer) # 최대 값 갱신
    
    move(arr) # 물고기 이동
    
    # 상어는 최대 3칸 갈 수 있음 (0은 자기 위치)
    for i in range(1, 4):
        nx, ny = x + dx[dir]*i, y + dy[dir]*i
        if nx < 0 or ny < 0 or nx >= 4 or ny >= 4 or arr[nx][ny] == -1:
            continue
        dfs((nx, ny), arr, shark)


answer = 0
shark = [0, (0,0), 0] # 누적 물고기, 좌표, 방향
arr = [[] for x in range(4)]
for i in range(4):
    data = list(map(int, input().split()))
    for j in range(0, 8, 2):
        num, d = data[j], data[j+1]
        arr[i].append([num, d])

dfs((0,0), arr, shark)
print(answer)
        
