'''
최단 경로 + 가중치 1인 경우 bfs 사용

인접 리스트로 표현된 그래프 : O(N+E)
인접 행렬로 표현된 그래프 : O(N^2) (이차배열)

큐 이용
1. 시작 노드를 큐에 넣고 방문 처리
2. 큐에서 노드 꺼낸 뒤 인접 노드 중 방문하지 않은 노드 큐에 넣기, 방문 처리
3. 2) 과정 반복
'''
from collections import deque

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    
    while q:
        now = q.popleft()
        print(now, end = ' ')
        
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

graph = [
      [],
      [2, 3, 8],
      [1, 7],
      [1, 4, 5],
      [3, 5],
      [3, 4],
      [7],
      [2, 6, 8],
      [1, 7]
]  # 1 2 3 8 7 4 5 6

visited = [False] * 9

bfs(graph, 1, visited) # 1 2 3 8 7 4 5 6