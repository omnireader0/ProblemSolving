import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
map = list(list(map(int, input().split())) for _ in range(n))
copymap = [[0]*m for _ in range(n)]
virus = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
answer = 0

for i in range(n):
    for j in range(m):
        if map[i][j] == 2:
            virus.append([i, j])

def bfs():
    q = deque(virus)
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if copymap[nx][ny] == 0:
                    copymap[nx][ny] = 2
                    q.append([nx, ny])
    
def get_space():
    space = 0
    for i in range(n):
        for j in range(m):
            if copymap[i][j] == 0:
                space += 1
    return space   
   
    
def make_wall(cnt):
    global answer
    
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                copymap[i][j] = map[i][j]
        
        bfs()
        answer = max(answer, get_space())
        return answer
            
    for i in range(n):
        for j in range(m):
            if map[i][j] == 0:
                map[i][j] = 1
                cnt += 1
                make_wall(cnt)
                map[i][j] = 0
                cnt -= 1
                
make_wall(0)
print(answer)