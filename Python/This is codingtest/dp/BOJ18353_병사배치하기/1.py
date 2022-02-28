n = int(input())
array = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[i] < array[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))


'''
가장 긴 증가하는 부분 수열
D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이

초기 테이블 1로 초기화
0<= j <i에 대하여 d[i] = max(d[i], d[j]+1) if array[j] < array[i]

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))

'''        