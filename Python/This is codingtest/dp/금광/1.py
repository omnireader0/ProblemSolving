t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = []
    for i in range(0, n*m, m):
        graph.append(list(arr[i:i+m]))
    
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                graph[i][j] += max(graph[i][j-1], graph[i+1][j-1])
            elif i == n-1:
                graph[i][j] += max(graph[i][j-1], graph[i-1][j-1])
            else:
                graph[i][j] += max(graph[i][j-1], graph[i-1][j-1], graph[i+1][j-1])
    max_value = 0
    for i in graph:
        max_value = max(i[-1], max_value)
    print(max_value)