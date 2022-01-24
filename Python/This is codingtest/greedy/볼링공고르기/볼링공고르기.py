n, m = map(int, input().split())
arr = list(map(int, input().split()))

balls = [0]*11

for i in arr:
    balls[i] += 1

answer = 0

for i in range(1, m+1):
    cnt = sum(balls[i+1:])
    answer += balls[i] * cnt
    
print(answer)
   
