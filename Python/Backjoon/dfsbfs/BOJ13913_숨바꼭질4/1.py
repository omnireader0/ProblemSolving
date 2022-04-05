from collections import deque
n, m = map(int, input().split())
check = [[-1, -1] for _ in range(100002)] # 최소 시간, 이전 방문 노드

q = deque()
q.append(n)
check[n][0] = 0

while q:
    v = q.popleft()
    
    if v == m:
        break
    
    for i in (v*2, v-1, v+1):
        if 0 <= i < 100001 and check[i][0] == -1:
            check[i][0] = check[v][0] + 1
            check[i][1] = v
            q.append(i)

print(check[m][0])
temp = []
temp.append(m)

while True:
    if check[m][1] != -1:
        temp.append(check[m][1])
        m = check[m][1]
    else:
        break
    
temp.reverse()
print(' '.join(map(str, temp)))

'''
check[[]] 2차 배열로 선언하고, 최소시간과 이전에 방문한 노드를 추적한다.
check[i][1] = v 이전에 방문한 노드를 저장해준다.
bfs한 후, temp라는 변수를 선언하여, check[k][1]부터 방문한 노드를 담아주고,
temp의 값이 거꾸로 담겨져 있으므로 역순으로 출력한다.
마지막에 join 함수는 리스트를 문자열로만 변환해주므로 int말고 str 쓰자!
'''