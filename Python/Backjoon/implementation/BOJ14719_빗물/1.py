h, w = map(int, input().split())

graph = list(map(int, input().split()))

max_h = max(graph)
max_idx = graph.index(max(graph))
temp1, temp2, result = 0, 0, 0
for i in range(max_idx+1): # max_index까지 더해줄 수를 찾아 누적
    if graph[i] > temp1: 
        temp1 = graph[i]
    result += temp1
for i in range(w-1, max_idx, -1):
    if graph[i] > temp2:
        temp2 = graph[i]
    result += temp2
print(result- sum(graph))