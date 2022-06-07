import sys
input = sys.stdin.readline
d, n, m = map(int, input().split())
distance = [d]
for _ in range(n):
    distance.append(int(input()))
distance.sort()
   
start = 0
end = d
result = 0

while start <= end:
    mid = (start + end) // 2 # gap
    cnt = 0
    current = 0
  
    for i in distance:
        if i - current >= mid:
            current = i
            cnt += 1
    
    if cnt >= n - m + 1:
        start = mid + 1
        result = max(result, mid)
    else:
        end = mid - 1
     
print(result)
    
'''
이분탐색을 통해 최소 거리의 최댓값을 mid로 구한다.  
각 이분 탐색을 할 때마다 돌을 제거하고, 제거한 돌의 개수가 m보다 작다면 start 를 mid + 1,
크다면 end를 mid -1로 갱신한다.
이때, 얿앤 돌의 개수가 m과 같다면 해당 값이 최소 거리가 되며, start를 +1 갱신한다.

'''