n, l, r= map(int, input().split())
map = list(list(map(int, input().split())) for _ in range(n))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] 
cnt = 0

def move(union, visited):
    average = sum(union)//len(union)
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 2:
                map[i][j] = average      

while True:
    visited = list([0]*n for _ in range(n))
    union = []
    idx = 0
    for i in range(n):
        for j in range(n):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < n and (l <= abs(map[i][j] - map[nx][ny]) <= r):
                    
                    if visited[i][j] == 0:
                        visited[i][j] = idx
                        union.append((map[i][j]))
                        idx += 1
                        
                    if visited[nx][ny] != idx:
                        visited[nx][ny] = idx
                        union.append((map[nx][ny]))
                
    if len(union) == 0:
        break
    move(union, visited)
    cnt += 1

print(cnt)
    
            
    



'''    
1. 국경 열기
- IF 인접한 나라간 인구차이가 범위안에 있다면, 국경 열고, 국경 열어둔 나라끼리 인구수 리스트에 담기
    - 방문처리 : 방문만 체크 1. 국경 열기 가능 2, 방문표시2인 경우 리스트에 담기
- ELSE 끝내기

2. 인구이동
- 방문표시2인 나라가 담긴 리스트를 매개변수로 받아서 적절하게 인구이동
- 리턴 카운트
- 방문 처리 리셋  

'''