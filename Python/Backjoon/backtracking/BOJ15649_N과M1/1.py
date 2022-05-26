# 전체 반복문에서 dfs 통해 작은 반복문을 돌게 됨
# 작은 반복문 완료되면 전체 반복문에서 남은 작업 처리해주기
'''
n,m = map(int, input().split())
arr = []
def dfs():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, n+1):
        if i not in arr:
            arr.append(i)
            dfs()
            arr.pop()
dfs()
'''

n,m = map(int, input().split())
v = [0]*8
visited = [0]*9

def dfs(depth):
    
    if depth == m:
        for i in range(m):
            print(v[i], end = ' ')
        print()
        return
    
    for i in range(1, n+1):
        if visited[i] == 0:
            visited[i] = 1
            v[depth] = i
            dfs(depth + 1)
            visited[i] = 0    

dfs(0)