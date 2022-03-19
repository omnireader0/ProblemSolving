n, m = map(int, input().split())
trees = list(map(int, input().split()))
answer = 0
left = 0
right = max(trees)
trees.sort(reverse=True)
while left <= right:
    mid = (left+right) // 2
    result = 0
    for i in trees:
        if i<mid:
            break
        result += i - mid
    if result >= m:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
print(answer)