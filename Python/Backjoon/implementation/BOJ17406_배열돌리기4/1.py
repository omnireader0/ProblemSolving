import copy
from collections import deque
from itertools import permutations
n, m, k = map(int,input().split())
graph = list(list(map(int, input().split())) for _ in range(n))
oper = list(list(map(int, input().split())) for _ in range(k))

def rotate(x, y, height, width):
    global c_graph
    q = deque()
    
    for i in range(y, y+width):
        q.append(c_graph[x][i])
    for i in range(x+1, x+height):
        q.append(c_graph[i][y+width-1])
    for i in range(y+width-2, y, -1):
        q.append(c_graph[x + height-1][i])
    for i in range(x+height-1, x, -1):
        q.append(c_graph[i][y])
    q.rotate(1)
    
    for i in range(y, y+width):
        c_graph[x][i] = q.popleft()
    for i in range(x+1, x+height):
        c_graph[i][y+width-1] = q.popleft()
    for i in range(y+width-2, y, -1):
        c_graph[x+height-1][i] = q.popleft()
    for i in range(x+height-1, x, -1):
        c_graph[i][y] = q.popleft()
    
min_value = int(1e9)
op_perm = list(permutations(oper))

for op in op_perm:
    c_graph = copy.deepcopy(graph)
    for r, c, s in op:
        left_x = r-s-1
        left_y = c-s-1
        
        height = 2*s + 1
        width = 2*s + 1
        while True:
            if height <= 0 or width <= 0:
                break
            rotate(left_x, left_y, height, width )
            left_x += 1
            left_y += 1
            height -= 2
            width -= 2
        
    for i in c_graph:
        min_value = min(min_value, sum(i))
    
print(min_value)
            