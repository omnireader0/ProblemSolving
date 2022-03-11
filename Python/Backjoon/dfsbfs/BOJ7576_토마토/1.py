from collections import deque
m, n = map(int, input().split())
graph = list( list(map(int, input().split())) for _ in range(n))
dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 1:
                q.append([x,y])    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < m  and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])
            
bfs()

cnt = 0
flag = True
for i in graph:
    cnt = max(max(i), cnt)
    if i.count(0) != 0:
        print(-1)
        flag = False
        break
   
if flag:
    print(cnt-1)

'''
bfs 끝나고, graph에 익지 않은 토마토가 남아있다면,
모두 익지 못하는 상황으로 본다.
이경우 -1을 출력하고 break로 빠져나온다!
'''