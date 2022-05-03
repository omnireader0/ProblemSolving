from sympy import O


def solution(info, edges):
    answer = 0
    n = len(info)
    graph = [[] for _ in range(n)]
    
    for edge in edges:
        r, c = edge
        graph[r].append(c)
        
    stack = [(1, 0, [0])]
    while stack:
        cur_sheep, cur_wolf, visited = stack.pop()
        answer = max(answer, cur_sheep)
        for cur_node in visited:
            for next_node in graph[cur_node]:
                if next_node not in visited:
                    next_sheep = cur_sheep
                    next_wolf = cur_wolf
                    if info[next_node]:
                        next_wolf += 1
                    else:
                        next_sheep += 1
                    if next_sheep <= next_wolf:
                        continue
                    stack.append((next_sheep,next_wolf,visited + [next_node]))            
    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))