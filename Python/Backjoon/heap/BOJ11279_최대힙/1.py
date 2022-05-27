import heapq
import sys
input = sys.stdin.readline
heap = []
for i in range(int(input())):
    x = int(input())
    
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])    
    else:
        heapq.heappush(heap, (-x, x))
        
'''
힙에 원소를 추가할 때 (-item, item)의 튜플 형태로 넣어주면 
튜플의 첫 번째 원소를 우선순위로 힙을 구성하게 된다.
원소 값의 부호를 바꿨기 때문에, 
최소 힙으로 구현된 heapq 모듈을 최대 힙 구현에 활용하게 되는 것이다.

힙에 push하면, 이렇게 들어간다. [(-5, 5), (-3, 3), (-1, 1)]
힙에서 pop할 때, 실제 원소 값은 튜플의 두번째 자리인 [1] 인덱싱으로 접근하면 된다. 
'''