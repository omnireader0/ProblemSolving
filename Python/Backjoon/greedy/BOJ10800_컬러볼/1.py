# import sys
# input = sys.stdin.readline
# n = int(input())

# colorball = []
# for i in range(1, n+1):
#     a, b = map(int, input().split())
#     colorball.append([i, a, b]) # 번호, 색, 크기


# colorball = sorted(colorball, key = lambda x : (x[2], x[1]))  # 크기, 색 정렬

# print(colorball)

# value = [0]*(n+1) # 색별 크기 누적
# total = 0
# for i in range(1, n+1):
    
#     idx = colorball[i][0]
#     print(total - value[idx])
#     value[idx] += colorball[i][2]
#     total += colorball[i][2]
#     print(total, value)

from collections import defaultdict
import sys


n = int(sys.stdin.readline())
ball = []
for i in range(n):
    c, s = map(int, sys.stdin.readline().split())
    ball.append([c, s, i])

# 공의 크기 순으로 정렬
ball.sort(key=lambda x: x[1])

answer = defaultdict(int)
ball_size_sum = defaultdict(int)  # 색깔 별 공의 크기 누적합

total = 0  # 총합
i, j = 0, 0
for i in range(n):
    while ball[j][1] < ball[i][1]:  # 크기가 작을 때까지 수행
        total += ball[j][1]
        ball_size_sum[ball[j][0]] += ball[j][1]
        j += 1
    answer[ball[i][2]] = total - ball_size_sum[ball[i][0]]  # 총합 - 현재 색깔 공 누적합

for i in range(n):
    print(answer[i])