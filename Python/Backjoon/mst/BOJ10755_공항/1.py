import sys
input = sys.stdin.readline
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a< b:
        parent[b] = a
    else:
        parent[a] = b

gate = int(input())
plane = int(input())
parent = [0]*(gate+1)
for i in range(1, gate+1):
    parent[i] = i
    
result = 0
for _ in range(gate):
    d = find(parent, int(input()))
    if d == 0:
        break
    union(parent, d, d-1) # 왼쪽집합과 합집합 연산
    result += 1
print(result)