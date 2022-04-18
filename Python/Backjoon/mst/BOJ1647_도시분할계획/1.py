import sys
input = sys.stdin.readline
n, m = map(int, input().split())
edges = []
for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
    
edges.sort()
last = 0

parent = [0]*(n+1)
for i in range(1, n+1):
    parent[i] = i

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a) 
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

answer = 0
max_c = 0
for edge in edges:
    c, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        answer += c
        max_c = max(max_c, c)
print(answer - max_c)
    