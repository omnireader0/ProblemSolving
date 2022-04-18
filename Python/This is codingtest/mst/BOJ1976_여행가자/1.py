import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
cities = list( list(map(int, input().split())) for _ in range(n))
plan = list(map(int, input().split()))

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

for i in range(n):
    for j in range(n):
        if cities[i][j] == 1:
            union(parent, i+1, j+1)

flag = True
for i in range(m-1):
    if find(parent, plan[i]) != find(parent, plan[i+1]):
        flag = False
if flag:
    print("YES")
else:
    print("NO")
    
    
'''
계획에 해당하는 경로가 같은 집합에 있는지 확인하면 된다.
따라서 두 노드 사이에 경로 존재하면 unionㅇ르 하여 노드의 연결성을 파악한다.
plan에 있는 노드를 꺼내 모두 같은 집합에 있는지 비교하여 리턴한다.
'''