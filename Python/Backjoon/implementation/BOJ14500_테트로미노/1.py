n, m = map(int, input().split()) # 세로 가로
graph = list( list(map(int, input().split())) for _ in range(n))
visited = [[False] * m for _ in range(n)]

maxValue = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# ㅗ 제외한 도형의 최댓값 계산
def dfs(i, j, sum_, cnt):
    global maxValue
    
    # 길이 4이면 최댓값 계산하고 리턴
    if cnt == 4:
        maxValue = max(maxValue, sum_)
        return 

    for a in range(4):
        nx = i + dx[a]
        ny = j + dy[a]
        
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, sum_ + graph[nx][ny], cnt+1)
            visited[nx][ny] = False

def ex(i, j):
    global maxValue
    for a in range(4):
        temp = graph[i][j]
        
        for k in range(3):
            # 세 곳만 확인하기 위해
            # 012 123 230 301
            b = (a+k) % 4
            nx = i + dx[b]
            ny = j + dy[b]
            
            # 날개 3개가 모두 셈이 되어야 하는데 그렇지 못한다면 빠져나오기
            if not (0 <= nx < n and 0 <= ny < m): 
                temp = 0
                break   
            temp += graph[nx][ny]       
        maxValue = max(maxValue, temp)

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, graph[i][j], 1)
        visited[i][j] = False
        ex(i, j)
print(maxValue)