from itertools import combinations
from copy import deepcopy

n = int(input())
corrider = list(list(map(str, input().split())) for _ in range(n))
spaces = []
teachers = []


for i in range(n):
    for j in range(n):
        if corrider[i][j] == 'X':
            spaces.append([i,j])
        if corrider[i][j] == 'T':
            teachers.append([i,j])
            
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def visit(): # 모든 선생에 대해 감시 피하기 성공 여부
    copy_corrider = deepcopy(corrider)
    for x,y in teachers:
        if not dfs(copy_corrider, x, y):
            return False
    return True
    
def dfs(copy_corrider, x,y): # 한 선생에 대해 감시 피하기 성공 여부
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        while True:
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                break
            if copy_corrider[nx][ny] == "O":
                break
            if copy_corrider[nx][ny] == "S":
                return False
            nx += dx[i]
            ny += dy[i]
    return True

# 메인        
firewall_combi = list(combinations(spaces, 3))


for firewall in firewall_combi:
    for x, y in firewall:
        corrider[x][y] = 'O'
    if visit():
        print("YES") 
        break
    for x, y in firewall:
        corrider[x][y] = 'X'
           
else : print("NO")

'''
1. 접근
치킨 배달과 비슷한 유형으로, 그래프 탐색으로 접근한다.
이때, 장애물을 배치하는 모든 경우에 대해 탐색해야 하므로, 조합과 백트래킹을 이용한다.

2. 검증
시간복잡도 : O(N^2C3)
복도의 길이는 n, 장애물을 선택하는 최대 경우의 수 n^2C3, dfs(감시피하기 성공 여부)는 n^2
O(N^2C3 + N^2)인데, n이 최대 6이므로 완전탐색으로 해결 가능하다.
공간복잡도 : 작음 
spaces 리스트 : 최대 30, teachers 리스트 : 최대 5, corrider/copy_corrider 최대 36, firewall_combi : 30C3
다 합쳐도 (30+5+36+30C3)B,  256MB에는 한참 못미침

3. 풀이
spaces 는 빈 공간 좌표 리스트
teachers는 선생님 좌표 리스트
firewall_combi는 spaces에서 3개씩 골라 구한 장애물 조합

메인
백트래킹 : 장애물을 설치하고 감시피하기 여부를 알아본 뒤, 장애물을 해제

def dfs(copy_corrider, x,y)
한 선생에 대한 감시 피하기 성공 여부를 알아본다.
선생이 이동한 자리에 학생이 있다면 감시 피하기가 실패한 것이다.

def visit()
모든 선생에 대한 감시 피하기 성공 여부를 알아본다.
복사한 그래프에 대해 dfs를 돌려서 모든 선생에 대해 감시 피하기의 성공 여부를 알아본다.
'''
            
