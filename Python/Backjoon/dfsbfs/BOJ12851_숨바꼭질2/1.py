from collections import deque
n, m = map(int, input().split())
arr = [0]*100001
check = [[-1, 0] for _ in range(100001)]

q = deque()
q.append(n)
check[n][0] = 0 # 최소 시간
check[n][1] = 1 # 방법의 수
while q:
    v = q.popleft()
    
    for i in (v-1, v+1, v*2):
        if 0 <= i < 100001:
            if check[i][0] == -1:
                q.append(i)
                check[i][0] = check[v][0] + 1 
                check[i][1] = check[v][1]
                
            elif check[i][0] == check[v][0] + 1: # 들른적 있으며, v에서 1초 걸려 i가 되는 경우
                check[i][1] += check[v][1] # 방법의 수 갱신

print(check[m][0])
print(check[m][1])

'''
시간복잡도 o(n)

노드를 처음 방문하는 경우와 한 번 이상 방문한 경우로 나누는데,
check[i][1] += check[v][1] 이 구문에서 누적 카운트가 증가하는 경우는 
i가 k일때일 것이고, 각 시간에 대한 방법의 수가 구해진다.
'''