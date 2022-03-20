n = int(input())
arr = list(map(int, input().split()))
INF = 1e9 * 2 +1
arr.sort()
left = 0
right = n-1
minSum = INF
answer = []

while left < right:
    now = arr[left] + arr[right]
    if abs(now) < minSum:
        minSum = abs(now)
        answer = [arr[left], arr[right]]
    if now >= 0:
        right -= 1
    else:
        left += 1
print(*answer)

'''
조심할 부분 - 42%에서 틀림
각 용액은   -1,000,000,000 이상 1,000,000,000 이하
이므로 , INF는 abs(두용액의 합)이며, 최대 1E9*2보다 커야 함.
'''