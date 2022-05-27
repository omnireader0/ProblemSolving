'''
중심 제외한 바깥쪽 방향 2개는 짝을 만들고,
중심을 차례대로 이동하면서 탐색한다.
'''
n, m = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(n))

dr = [(0,1), (-1,0), (-1,0), (0,1)]
dc = [(-1,0), (0,-1), (0,1), (1,0)]

visited = [[0]*m for _ in range(n)]

max_value = 0
def dfs(idx, value):
    global max_value
    
    if idx == n*m:
        max_value = max(max_value, value)
        return
    
    r = idx//m
    c = idx%m
    
    if not visited[r][c]:
        for i in range(4):
            r1 = r + dr[i][0]
            c1 = c + dc[i][0]
            r2 = r + dr[i][1]
            c2 = c + dc[i][1]
            
            if r1 < 0 or r1 >= n or c1 < 0 or c1 >= m or r2 < 0 or r2 >= n or c2 < 0 or c2 >= m: continue
            if visited[r1][c1] or visited[r2][c2]: continue
            
            visited[r][c] = 1
            visited[r1][c1] = 1
            visited[r2][c2] = 1
            
            dfs(idx+1, value + arr[r][c] * 2 + arr[r1][c1] + arr[r2][c2])
            
            visited[r][c] = 0
            visited[r1][c1] = 0
            visited[r2][c2] = 0
    
    dfs(idx+1, value)
    
dfs(0, 0)
print(max_value)