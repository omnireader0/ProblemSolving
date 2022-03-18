import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
def dfs1(x): # 나보다 키 큰 사람
    global cnt1
    visited[x] = 1
    for i in graph1[x]:
        if not visited[i]:
            cnt1 += 1
            dfs1(i)
    return cnt1
            
def dfs2(x): # 나보다 키 작은 사람
    global cnt2
    visited[x] = 1
    for i in graph2[x]:
        if not visited[i]:
            cnt2 += 1
            dfs2(i)
    return cnt2

n, m = map(int, input().split())
graph1 = [[] for _ in range(n+1)]
graph2 = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph1[a].append(b)
    graph2[b].append(a)

result, answer = 0, 0
for i in range(1, n+1):
    cnt1, cnt2 = 0, 0
    visited = [0]*(n+1)
    result = dfs1(i)
    visited = [0]*(n+1)
    result += dfs2(i)
    
    if result == n-1: # 본인 제외 하고 다른 모두와 키 순서를 비교했다면
        answer += 1
print(answer)

'''
플로이드워셜보다 훨씬 빠르긴 하다.
4배 정도 빠름
'''