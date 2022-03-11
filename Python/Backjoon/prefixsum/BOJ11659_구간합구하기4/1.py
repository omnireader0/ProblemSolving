import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
dp = [0]* (n+1)
dp[1] = arr[1]
for i in range(2, n+1):
    dp[i] = arr[i] + dp[i-1]
for _ in range(m):
    a, b = map(int, input().split())
    print(dp[b]- dp[a-1])

'''
접두사 합을 이용하는 경우, 쿼리당 계산시간은 O(1)이 된다. 
그 이유는 N개의 수의 위치 각각에 대해 접두사 합을 미리 구해놓기 때문이다. 
결과적으로 N개의 데이터와 M개의 쿼리가 있을 때, 
전체 구간 합을 모두 계산하는 작업은 O(N+M)의 시간복잡도를 가진다.
'''