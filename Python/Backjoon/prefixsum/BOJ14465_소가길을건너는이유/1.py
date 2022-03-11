import sys
input = sys.stdin.readline

n, k, b = map(int, input().split())
dp = [0]*(n+1)
for i in range(b):
    dp[int(input())] = 1

for i in range(1, n+1):
    dp[i] += dp[i-1]

answer = 1e9
for i in range(1, n-k+2):
    answer = min(answer, dp[i+k-1] - dp[i-1])
print(answer)

'''
슬라이딩 윈도우 + dp를 적용
dp는 고장난 신호등 만날 때 마다 개수 누적
최대 k개의 연속된 신호등을 가져야 하므로 슬라이딩 윈도우 사이즈를 k로 지정
슬라이딩 윈도우를 오른쪽으로 한 칸씩 옮겨가면서, 
슬라이딩 윈도우 안에 있는 고장난 신호등의 개수를 센다.
그중에서 가장 min인 경우를 구해서 출력해주면 됨

    1 2 3 4 5 6 7 8 9 10
dp  1 2 2 2 3 3 3 3 4 5

'''