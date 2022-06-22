'''
hhhhh
ttthh
thhth
ttttt

뒤집은 동전의 개수가 중요하지, 동전의 위치가 중요하지는 않다.



'''
from collections import deque 

n, k = map(int, input().split())
coin = list(input())
b_cnt = coin.count('T')
q = deque([])
q.append((b_cnt, 0))
visited = [False] * (n+1) # t개수를 방문했는지 체크
flag = False
while q:
    # t개수, 뒤집기 횟수
    b, cnt = q.popleft()
    f = n - b 
    
    if b == n:
        flag = True
        break
    
    if visited[b]:
        continue
    
    visited[b] = True
    
    # 뒤집기 -> 앞면 i개, 뒷면 k-i개 뒤집는데, 
    for i in range(k+1):
        if f >= i and b >= k-i and not visited[b - (k-i)+ i]:
            q.append((b - (k-i)+ i,  cnt + 1))
    
       
if flag:
    print(cnt)
else:
    print(-1)

