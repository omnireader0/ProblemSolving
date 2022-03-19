n, m = map(int, input().split())
arr = list(map(int, input().split()))
left = 0
right = 0
result = 0
while right <= n-1 and left <= n-1:
    if sum(arr[left:right+1]) < m:
        right += 1
    
    elif sum(arr[left:right+1]) == m:
        result += 1
        right += 1
    else:
        left += 1
print(result)
    