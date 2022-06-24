'''

'''
#https://boomrabbit.tistory.com/183
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def dfs(x, y, dir, cnt):
    global answer
    if cnt >= n:
        return
    
    nd = [(dir - 1) % 6, (dir + 1) % 6]
    for idx in nd:
        di = d[idx]
        nx, ny = x + di[0], y + di[1]
        if not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, idx , cnt + 1)
            visited[nx][ny] = 0
        elif cnt + 1 == n:
            answer += 1

n = int(input())

visited = [[0 for _ in range(60)] for _ in range(60)]
d = [(-2, 0), (-1, 1), (1, 1), (2, 0), (1, -1), (-1, -1)]
answer = 0
visited[30][30] = True
visited[28][30] = True
dfs(28, 30, 0, 0)
print(answer)