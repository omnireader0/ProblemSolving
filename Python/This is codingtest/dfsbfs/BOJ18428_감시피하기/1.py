# 실패한 코드
from itertools import combinations
from collections import deque
from copy import deepcopy

n = int(input())
corrider = list(list(map(str, input().split())) for _ in range(n))
spaces = []
teachers = []
# students = []

for i in range(n):
    for j in range(n):
        if corrider[i][j] == 'X':
            spaces.append([i,j])
        if corrider[i][j] == 'T':
            teachers.append([i,j])
        # if corrider[i][j] == 'S':
        #     students.append([i,j])
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def visit():
    copy_corrider = deepcopy(corrider)
    for x, y in teachers:
        check = bfs(copy_corrider, x, y)
        if  check:
            print(copy_corrider, '-')
            return True
    print(copy_corrider)
    return False

def bfs(copy_corrider, x, y):
    q = deque()
    for i in range(4):
        q.append([x, y])
        while q:
            a, b = q.popleft()
            nx = a + dx[i]
            ny = b + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                print(nx, ny)
                if copy_corrider[nx][ny] == 'X':
                    copy_corrider[nx][ny] = 'T'
                    q.append([nx, ny])
                elif copy_corrider[nx][ny] == 'S':
                    return False
                elif copy_corrider[nx][ny] == 'O':
                    break  
            else:
                break
    return True
        
firewall_combi = list(combinations(spaces, 3))

flag = False
for firewall in firewall_combi:
    for x, y in firewall:
        corrider[x][y] = 'O'
    if visit():
        flag = True
        break
    for x, y in firewall:
        corrider[x][y] = 'X'
           
if flag : print("YES") 
else : print("NO")

# [['S', 'S', 'S', 'T'], ['O', 'O', 'O', 'X'], ['X', 'X', 'X', 'X'], ['T', 'T', 'T', 'X']]

'''
풀이
- T, S, O의 좌표를 리스트에 담는다.
- 3개의 장애물을 세운다.( 장애물 설치가 가능한 경우의 수를 조합으로 구해서 설치)
- T는 장애물이 없는 곳이라면 어디든 방문할 수 있다. BFS로 구현한다.
- 남아 있는 S의 수를 세어서, 감시 피하기 여부를 파악한다. 
'''
            
