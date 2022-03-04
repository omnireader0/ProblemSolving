n = int(input())
step = [0]*301
dp = [0]*301
for i in range(n):
    step[i] = int(input())
    
dp[0] = step[0]
dp[1] = step[0] + step[1]
dp[2] = max(step[0]+step[2], step[1]+step[2])
for i in range(3, n):
    dp[i] = max(dp[i-2]+step[i], dp[i-3]+step[i-1]+step[i])

print(dp[n-1])