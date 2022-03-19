n, m, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.append(0)
arr.append(l)
arr.sort()
left = 1
right = l-1

def count(l):
    cnt = 0
    for i in range(1, n+2):
        cnt += (arr[i]-arr[i-1]-1) // l
    return cnt

while left <= right:
    mid = (left + right) // 2
    if count(mid) <= m:
        result = mid
        right = mid -1
    else:
        left = mid + 1
print(result)

'''
어려운 문제다. 이분 탐색을 적용한다는 아이디어도 아직 이해를 못한 것 같다.

이 문제는 전체 도로 길이를 이분 탐색을 반복 하여 휴게소 사이의 거리를 찾아낸다.
이분탐색으로 구한 휴게소 사이의 거리를 mid라고 했을 때, 
각 휴게소의 거리/mid를 하여 몇개의 휴게소를 더 세울 수 있는지 count하고,
이 count한 개수가 m보다 크다면 mid의 간격을 넓히고, 
반대로 개수가 m보다 작다면 mid의 간격을 좁혀나간다.

'''