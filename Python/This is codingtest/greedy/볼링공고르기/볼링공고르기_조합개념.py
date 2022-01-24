n, m = map(int, input().split())
arr = list(map(int, input().split()))

balls = [0]*11

for i in arr:
    balls[i] += 1
    
answer = n*(n-1)//2    

duplicate = 0
for i in range(1, m+1):
    if balls[i] > 1:
        duplicate += balls[i]*(balls[i] -1)//2 
print(answer - duplicate)
