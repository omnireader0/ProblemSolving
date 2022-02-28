n,m = map(int, input().split())
array = [[1e9]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            array[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    array[a][b] = 1
    array[b][a] = 1
    
x, k = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            array[a][b] = min(array[a][b], array[a][k]+ array[k][b])

answer = array[1][k] + array[k][1]
if answer >= 1e9:
    print(-1)
else:
    print(answer) 