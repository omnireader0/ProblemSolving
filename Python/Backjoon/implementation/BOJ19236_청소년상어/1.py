import copy
from re import L
from unittest import result

# 4 X 4 크기 격자에 존재하는 각 물고기의 번호(없으면 -1)와 방향 값을 담는 테이블
array = [[None]*4 for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        # 각위치마다 [물고기 번호, 방향] 
        array[i][j] = [data[j*2], data[j*2+1]-1]
        
# 방향  ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 현재 위치에서 왼쪽으로 회전된 결과 반환
def turn_left(direction):
    return (direction + 1) % 8

def find_fish(array, idx):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == idx:
                return (i, j)
    return None

# 모든 물고기를 회전 및 이동시킴
def move_all_fishes(array, now_x, now_y):
    # 1번부터 16번까지 차례대로 
    for i in range(1, 17):
        # 해당 물고기 위치 찾기
        position = find_fish(array, i)
        
        if position != None:
            x, y = position[0], position[1]
            direction = array[x][y][1]
            
            # 방향을 반시계로 회전시키면서 이동 가능한지 확인
            for j in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                
                # 해당 방향으로 이동이 가능하다면 이동 시키기
                if 0 <= nx < 4 and 0 <= ny < 4:
                    if not (nx == now_x and ny == now_y):
                        array[x][y][1] = direction
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                        break
                direction = turn_left(direction)
            
def get_possible_positions(array, now_x, now_y):
    positions = []
    direction = array[now_x][now_y][1]
    
    # 현재의 방향으로 쭉 이동
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        # 범위를 벗어나지 않는지 확인하며
        if 0 <= now_x and now_x < 4 and 0 <= now_y and now_y < 4:
            # 물고기가 존재하는 경우
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    return positions
        
        
result = 0

# 모든 경우를 탐색 dfs
def dfs(array, now_x, now_y, total):
    global result
    array = copy.deepcopy(array)
    
    total += array[now_x][now_y][0] # 현재 위치의 물고기 먹는다.
    array[now_x][now_y][0] = -1 # 먹음 표시
    
    move_all_fishes(array, now_x, now_y) # 전체 물고기 이동
    
    # 이제 상어가 이동할 차례, 이동 가능한 위치 찾기
    positions = get_possible_positions(array, now_x, now_y)
    #
    # 이동할 수 있는 위치가 하나도 없다면 종료
    if len(positions) == 0:
        result = max(result, total) # 최댓값 저장
        return 
    # 모든 이동할 수 있는 위치로 재귀적으로 수행
    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)
    
    
dfs(array, 0, 0, 0)
print(result)
