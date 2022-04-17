import sys
input = sys.stdin.readline

n = int(input())
parent = [0]*(n+1)
edges = []
result = 0

for i in range(1, n+1):
    parent[i] = i

x = []
y = []
z = []

for i in range(1, n+1):
    d = list(map(int, input().split()))
    x.append((d[0], i))
    y.append((d[1], i))
    z.append((d[2], i))

x.sort()
y.sort()
z.sort()    

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
    
# 인접한 노드들로부터 간선 정보를 추출
for i in range(n-1):
    # 비용순으로 정렬 -> 첫 번째는 원소 비용
    edges.append((x[i+1][0]-x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0]-y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0]-z[i][0], z[i][1], z[i+1][1]))
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost
print(result)

'''
mst적용하여 O(ElogE)로 문제를 해결한다.

이 문제에서 노드는 최대 십만, 이므로 간선의 개수는 십만(십만-1)/2이다.
이것을 모두 비교하면 시간초과 발생하므로, 세 축을 기준으로 정렬 수행하는 아이디어를 적용한다.

입력을 세축으로 받는데, 세 축에 대해 각각 정렬하고,
X축 -1, 10, 11, 14, 19 이런식이 된다.
결과적으로 각 행성간 차이는 11, 1, 3, 5가 되는데 이것을 정렬은 한다.
결국 4개의 간선만 고려하면 되는 것이다.
총 고려해야 하는 간서의 개수는 3(N-1)이 되며
각 축에 대해 N-1개의 간선만 이용해도 최소 신장 트리를 만들 수 있다는 점을 알 수 있다.
'''