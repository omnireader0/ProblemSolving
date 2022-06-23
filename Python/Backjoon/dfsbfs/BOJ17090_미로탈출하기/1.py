'''
dfs로만 해결할 수 없음
최대 그래프 크기 500*500 = 2500000
최대 250000 ^2 탐색하면 TLE 뜰 것임

dp + dfs
방문 표시 dp 테이블 생성
이미 방문한 적이 있는 칸은 다시 탐색할 필요 없음
방문한 적 없음 -1
방문표시 0
방문하였고, 탈출 가능 1
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
n, m = map(int, input().split())
maze = list(list(input()) for _ in range(n))

# U R D L
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


dp = [[-1]*m for _ in range(n)]

def dfs(x, y):
    
    # 방문했다면 다시 탐색 필요 x
    if dp[x][y] != -1:
        return dp[x][y]
    
    # 방문 표시
    dp[x][y] = 0
    di = maze[x][y]
    if di == 'U':
        d = 0
    elif di == 'R':
        d = 1
    elif di == 'D':
        d = 2
    else:
        d = 3
    nx = x + dx[d]
    ny = y + dy[d]
    
    # 탈출 가능하다면
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        dp[x][y] = 1
    else: # 더 탐색
        dp[x][y] = dfs(nx, ny)
    
    return dp[x][y]
    
          
answer = 0
for i in range(n):
    for j in range(m):
        result = dfs(i, j)
        if result == 1: 
            answer += 1
print(answer)
