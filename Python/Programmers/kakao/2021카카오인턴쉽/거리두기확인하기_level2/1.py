from collections import deque
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def bfs(place, x, y):
    
    visit = [] 
    q = deque()
    q.append((x, y, ""))
    visit.append((x,y))
    
    while q:
        x, y, dist = q.popleft()
        if dist == 'P' or dist == 'OP':
            return 0
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= 5 or ny<0 or ny >= 5 or (nx, ny) in visit or len(dist) >= 2:
                continue
            
            q.append((nx, ny, dist+place[nx][ny]))
            visit.append((nx, ny))
    return 1
    
    
def solution(places):
    answer = []
    for i in range(5):
        flag = 1
        for j in range(5):
            for k in range(5):
                if places[i][j][k] == "P":
                    flag = bfs(places[i], j, k)
                    if flag == 0:
                        break
            if flag == 0:
                break
        answer.append(flag)
    return answer