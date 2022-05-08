n = int(input())
developers = list(map(int, input().split()))

left = 0
right = n-1
max_value = 0
while left < right:
    value = (right - left-1) * min(developers[left], developers[right])
    max_value = max(value, max_value)
    if developers[left] > developers[right]:
        right -= 1
    else:
        left += 1
print(max_value)
    