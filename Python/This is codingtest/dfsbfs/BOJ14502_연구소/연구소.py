'''
0 빈 칸
1 벽
2 바이러스
안전영역 최댓값

벽 세우고 -> dfs로 바이러스 퍼뜨리기 -> 안전영역 크기 세기
원본 맵 잃지 않기 위해 맵 복사 필요(3개 벽 세워진 맵을 복사)
'''

n, m = map(int, input().split())
map = list(list(map(int, input().split())) for _ in range(n))
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
copymap = [[0]*m for _ in range(n)]
answer = 0

def spread_virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if copymap[nx][ny] == 0:
                copymap[nx][ny] = 2
                spread_virus(nx, ny)
            
def get_space():
    space = 0
    for i in range(n):
        for j in range(m):
            if copymap[i][j] == 0:
                space += 1
    return space
    
def dfs(cnt):
    global answer
    # 벽 3개 만들면 바이러스 퍼뜨리기와 안전영역 구하기
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                copymap[i][j] = map[i][j]
    
        for i in range(n):
            for j in range(m):
                if copymap[i][j] == 2:
                    spread_virus(i, j)
        answer = max(answer, get_space())
        return answer
    
    # 벽 세우기 -> 백트래킹으로 원본맵을 보호
    for i in range(n):
        for j in range(m):
            if map[i][j] == 0:
                map[i][j] = 1
                cnt += 1
                #print(1, map)
                dfs(cnt)
                map[i][j] = 0
                #print(2, map)
                cnt -= 1
                
dfs(0)
print(answer)