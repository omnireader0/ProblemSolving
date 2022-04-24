import sys
input = sys.stdin.readline
n, m = map(int, input().split())
domain = [list(map(int, input().split())) for _ in range(n)]

prefix_sum = [[0]*(m+1) for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        prefix_sum[i+1][j+1] = prefix_sum[i][j+1] + prefix_sum[i+1][j] - prefix_sum[i][j] + domain[i][j]
          

k = int(input())
for _ in range(k):
    a, b, c, d = map(int, input().split())
    print(prefix_sum[c][d]-prefix_sum[a-1][d]-prefix_sum[c][b-1]+prefix_sum[a-1][b-1])
    
    
'''
미리 누적합 구해놓고,
조건이 주어졌을 때의 누적합을 찾는다!
'''
    