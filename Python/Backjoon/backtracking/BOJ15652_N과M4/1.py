n ,m = map(int, input().split())
arr = []

def dfs(idx):
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(idx, n+1):
        arr.append(i)
        dfs(i)
        arr.pop()
dfs(1)

'''
결과가 비내림차순이라는 것에 주의한다.
'''