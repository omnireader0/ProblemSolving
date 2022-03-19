n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
left = 1
right = arr[-1] - arr[0]
result = 0

while left <= right:
    mid = (left + right)//2
    prev = arr[0]
    cnt=1
    
    for i in range(1, n):
        if arr[i] - prev >= mid:
            cnt += 1
            prev = arr[i]
    
    if cnt >= m:
        result = max(result, mid)
        left = mid + 1
    else:
        right = mid -1

print(result)