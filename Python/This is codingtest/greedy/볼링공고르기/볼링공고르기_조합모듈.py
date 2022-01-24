from itertools import combinations

n,m = map(int, input().split())
balls = list(map(int, input().split()))

answer = 0

for a, b in combinations(balls, 2):
    if a != b:
        answer += 1
print(answer) 