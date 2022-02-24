import heapq
n = int(input())

heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)
result = 0

while len(heap) != 1:
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    z = x + y
    result += z
    heapq.heappush(heap, z)

print(result)