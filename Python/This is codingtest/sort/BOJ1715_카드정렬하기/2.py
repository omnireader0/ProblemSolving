from heapq import *
l=[]
for _ in range(int(input())):
    heappush(l,int(input()))
a=0
while len(l)>1:
    t=heappop(l)+heappop(l)
    a+=t
    heappush(l,t)
print(a)

'''
접근

가장 작은 두 카드를 더했을 때 최솟값이 보장됨
따라서 최소 힙을 이용해 가장 작은 값이 우선순위 높도록 정렬
'''