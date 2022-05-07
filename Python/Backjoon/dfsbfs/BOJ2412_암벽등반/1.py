'''
최소 이동 횟수를 구하기 위해 bfs
graph를 set으로 한 이유는 set이 빨라서 시간 초과 문제 해결
이동 방향 정보는 dx, dy로 설정하고, 이중 반복문을 통해 다음 방문할 좌표 구한다.
방문이 가능하다면 큐에 [좌표, 이동횟수 +1]를 삽입하고 큐가 빌 때까지 방문한다.
같은 좌표을 방문할 수 없기 때문에 graph에서 방문한 좌표는 삭제한다.
'''

import sys
from collections import deque
input =sys.stdin.readline
n, t = map(int, input().split())

graph = set()
for _ in range(n):
    x, y = map(int, map(int, input().split()))
    graph.add((x,y))
    
dx = [-2, -1, 0, 1, 2]
dy = [-2, -1, 0, 1, 2]

q = deque()
q.append([0,0,0]) # 좌표, 이동 횟수
check = False
while q:
    x, y, cnt = q.popleft()
    if y == t:
        check = True
        break
    for i in range(5):
        for j in range(5):
            nx = x + dx[i]
            ny = y + dy[j]
            if (nx, ny) in graph:
                q.append([nx, ny, cnt+1])
                graph.remove((nx, ny))
if check:
    print(cnt)
else:
    print(-1)