n, m, r = map(int, input().split())
graph = list(list(map(int, input().split()))for _ in range(n))

# 우 하 좌 상
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def rotate(idx, len):
    
    rr = r % len
    for _ in range(rr):
        
        start_num = graph[idx][idx]
        x = idx
        y = idx
        
        d = 0
        while d < 4:
            nx = x + dx[d]
            ny = y + dy[d]
            
            if nx== idx and ny == idx:
                break
            
            if idx <= nx < n-idx and  idx <= ny < m-idx: 
                # 반시계 방향으로 옮김
                graph[x][y] = graph[nx][ny]
                x = nx
                y = ny
            else: # 방향 전환
                d += 1
        graph[idx+1][idx] = start_num

cnt = min(n,m)//2
nn = n
mm = m

for i in range(cnt):
    rotate(i, 2*(nn+mm)-4)
    nn -= 2
    mm -= 2
    
for i in range(n):
    for j in range(m):
        print(graph[i][j], end=' ')
    print()
    