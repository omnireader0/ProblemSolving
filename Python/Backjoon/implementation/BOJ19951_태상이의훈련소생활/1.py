import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
temp = [0]*n
for _ in range(m):
    a, b, c = map(int, input().split())
    temp[a-1] += c
    if b < n:
        temp[b] -= c

dp = [0]*(n)
dp[0] = temp[0]
for i in range(1, n):
    dp[i] = dp[i-1] + temp[i]
    
for i in range(n):
    print(dp[i]+arr[i], end = ' ')
    
'''

참고 : https://hsdevelopment.tistory.com/772

n과 m의 크기가 최대 십만이기 때문에 누적합 아이디어로 해결합니다.
(n 십만, m십만 이라면 o(n*m) = 10^12이므로 탐색하면 시간 초과 발생)
연병장 높이 배열을 입력받고, 새로운 배열 temp(연병장 배열 사이즈)를 만들어서 아래처럼 활용합니다.
temp는
i번 원소부터 j번 원소까지 각각 k 를 더한다면,
i번 원소에 k 더하고, j+1 원소에 k를 뺍니다.
temp에 있는 배열의 값을 이용해 누적합을 구하고,
최종적으로 각 인덱스에 해당하는 누적합 값과 연병장 높이 배열의 값을 합하면 o(n)에 해결할 수 있습니다.

'''