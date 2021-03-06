from heapq import *
heap=[]
for _ in range(int(input())):
    heappush(heap,int(input()))
answer=0
while len(heap)>1:
    data = heappop(heap)+heappop(heap)
    answer += data
    heappush(heap, data)
print(answer)

'''
접근

가장 작은 두 카드를 더했을 때 최솟값이 보장됨
따라서 최소 힙을 이용해 가장 작은 값이 우선순위 높도록 정렬
'''