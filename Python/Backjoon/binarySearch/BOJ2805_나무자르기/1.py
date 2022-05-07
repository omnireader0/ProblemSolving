'''
파라메트릭 서치 유형의 문제
최적화 문제를 결정문제로 바꿔 해결한다.
원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제에 주로 사용한다.

어떤 높이로 잘랐을 때 조건을 만족 여부에 따라 yes/no로 탐색 범위를 좁혀서 문제를 해결할 수 있다.
높이는 1~10억이므로, 탐색 범위가 넓은 경우 이진탐색으로 접근을 한다.

시간복잡도
높이를 이진탐색으로 찾는다면, log(2)10억 = 30, 약 30번 만에 높이를 찾을 수 있다.
떡의 개수가 100만개 이므로 최대 3000만번의 연산이 이루어진다.
'''
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