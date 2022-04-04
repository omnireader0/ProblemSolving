from collections import deque
n, k = map(int, input().split())
graph = [0]*100001

cnt = 0
q = deque()
q.append(n)

while q:    
    v = q.popleft()
    if v == k:
        print(graph[k])
        break
    
    for i in (v-1, v+1, v*2):
        if 0 <= i < 100001 and graph[i] == 0:
            graph[i] = graph[v] + 1
            q.append(i)

'''
100000의 길이 점을 방문하여, 동생의 위치를 찾는다. 
매번 x-1, x+1, 2*x 3가지 경우에 대해 방문 처리를 한다.
이떄 큐를 이용한 bfs로 해결한다. 
'''