import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent , b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    village = []    
    for i in range(n):
        x, y, z = map(int, input().split())
        village.append((z, x, y))
    village.sort()

    parent = [0]*(m)
    for i in range(m):
        parent[i] = i
    
    answer = 0
    result = 0
    for v in village:
        cost, a, b = v
        answer += cost
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            result += cost
            
    print(answer-result)



