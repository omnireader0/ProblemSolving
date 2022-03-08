def fibonacci(n):
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] 
    return dp
    
t = int(input())
for _ in range(t):
    n = int(input())
    if n == 0: print(1, 0)
    elif n == 1: print(0, 1)
    else: 
        answer = fibonacci(n)
        print(answer[n-2], answer[n-1])    
        
'''
규칙
n  zero  one
0   1   0
1   0   1
2   1   1
3   1   2
4   2   3
5   3   5
6   5   8
7   8   13
8   13  21
'''