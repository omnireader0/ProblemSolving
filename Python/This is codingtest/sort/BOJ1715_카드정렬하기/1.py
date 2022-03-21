import heapq

n = int(input())
heap = []
for i in range(n):
    heapq.heappush(heap, int(input()))

result = 0
while len(heap) > 1:
    data = heapq.heappop(heap) + heapq.heappop(heap)
    result += data
    heapq.heappush(heap, data)
print(result)

'''
접근

가장 작은 두 카드를 더했을 때 최솟값이 보장됨
따라서 최소 힙을 이용해 가장 작은 값이 우선순위 높도록 정렬
'''
