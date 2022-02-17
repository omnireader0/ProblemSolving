'''
인접 리스트로 표현된 그래프 : O(N+E)
인접 행렬로 표현된 그래프 : O(N^2) (이차배열)

2가지 방법 : 스택, 재귀

스택
1) 시작 노드를 스택에 삽입하고 방문 처리
2) 스택의 최상단 노드에 방문하지 않은 인접 노드 있으면, 스택에 넣고 방문 처리
방문하지 않은 인접 노드 없다면, 스택에서 최상단 노드 꺼내기
3) 2번의 과정을 수행할 수 없을 때까지 반복

재귀
1. 현재 노드가 방문한 적 있다면 리턴
1. 현재 노드를 방문 처리
2. 현재 노드의 인접 노드 재귀 탐색
'''

# 스택
def dfs_stack(graph, start):
    stack = []
    visited = []
    
    stack.append(start)
    
    while stack:
        now = stack.pop()
        if now not in visited:
            visited.append(now)
            stack.extend(graph[now])           
            
    return ' '.join(visited)

# 재귀
visited = []
def dfs_recursive(graph, start):
    
    if start in visited:
        return 
    
    visited.append(start)
    print(start, end= ' ')
    
    for i in graph[start]:
        dfs_recursive(graph, i)
    

graph = {
    'A': ['B'],
    'B': ['A', 'H', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

print(dfs_stack(graph, 'A'))  
print(dfs_recursive(graph, 'A'))