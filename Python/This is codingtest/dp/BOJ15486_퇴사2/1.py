import sys
input = sys.stdin.readline
n = int(input())
t = [0]*n
p = [0]*n
for i in range(n):
    t[i], p[i] = map(int, input().split())
dp = [0]*(n+1)

for day in range(n-1, -1, -1):
    if t[day] + day <= n:
        # 오늘 상담하는 경우의 기댓값과 내일 상담하는 경우의 기댓값 비교
        dp[day] = max(dp[day + t[day]]+p[day] , dp[day+1])
    else:
        dp[day] = dp[day+1]
print(dp[0])


'''
dp[day] = max(dp[day+1], dp[day + t[day]] + p[day] ) 

dp[day] : 0일 ~ day까지 최댓값을 저장하는 테이블로,

​				  퇴사일까지 최댓값을  DP테이블에 저장하도록 한다.

dp[day]는 최댓값을 구하기 위해 2가지 경우로 나눠서 생각한다.

1. 오늘 상담을 한다 dp[day + t[day]] + p[day]  (오늘 한 상담이 완료되는 날에 받을 수 있는 금액)
2. 오늘 하지 않는다  dp[day + 1]  (오늘 말고 다음날 한 상담에서 받을 수 있는 금액 기대)

| day                   | 0    | 1    | 2    | 3    | 4    | 5    | 6    |
| --------------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| t : 완료 기간         | 3    | 5    | 1    | 1    | 2    | 3    | 2    |
| p : 완료 금액         | 10   | 20   | 10   | 20   | 15   | 40   | 200  |
| dp : 누적 기대 최대값 | 45   | 45   | 45   | 35   | 15   | 0    | 0    |

sol(0) = max(sol(1), sol(3) + 10)

sol(1) = max(sol(2), sol(6) + 20)

sol(2) = max(sol(3), sol(3) + 10)

sol(3) = max(sol(4), sol(4) + 20)

sol(4) = max(sol(5), sol(6) + 15)

sol(5) = max(sol(6), sol(8) + 40)

sol(6) = max(sol(7), sol(8) + 200)

solve(7) = 0  퇴사

solve(8) = 음수무한대 -> 6일날까지 일하고 끝내야 하는데, 

점화식 sol(5) , sol(6)에서 max로 값을 구하므로, sol(6), sol(7)의 값이 max로 취해져야 한다. 

그러므로, sol(8)은 음수무한대로 초기화해주면 점화식을 만족하게 된다.

**거꾸로 올라가면 sol(0)의 값을 구할 수 있고, 퇴사전까지의 최댓값이 된다**.

dp는 이미 구한값을 반복하지 않아서 연산을 단축시키는데,

위에서부터 아래로 call해서 sol(6)을 구하고, sol(6)에서 return해준 값을  이용하여

거슬러 올라가면 sol(0)의 값을 구할 수 있다. 

'''