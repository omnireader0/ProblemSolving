import sys
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
min_value = int(1e9)
result = []
for i in range(n-2):
    temp = arr[i]
    left = i+1
    right = n-1
    while left < right:
        curr = temp + arr[left] + arr[right]
        if abs(curr) <= abs(min_value):
            min_value = curr
            result = [temp, arr[left], arr[right]]
        if curr < 0:
            left += 1
        elif curr > 0:
            right -= 1
        else:
            break
    break
print(result[0],result[1], result[2])
            