from collections import deque

n, m = map(int, input().split())
q = deque()
q.append(n)
check = [-1]*100001
check[n] = 0

while q:
    v = q.popleft()
    
    if v == m:
        print(check[v])
        break
    
    if 0 <= v*2 < 100001 and check[v*2] == -1:
        check[v*2] = check[v]
        q.append(v*2)
        
    for i in (v-1 ,v+1):
        if 0 <= i < 100001 and check[i] == -1:
            check[i] = check[v] + 1
            q.append(i)

'''
check[] 를 이용해 방문처리 & 최소시간누적을 동시에 한다.
순간이동 하는 if문을 선두에 배치한다.
그 이유는 n=2, k=4일때 count=0이 되어야 하는데, 
걷는 if문이 순간이동 if문보다 먼저 나오면 오답이 나온다.
'''