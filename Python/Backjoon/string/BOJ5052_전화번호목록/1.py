import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    numbers = []
    for _ in range(n):
        numbers.append(input().strip())
    numbers.sort()
    flag = True
    for i in range(n-1):
        if numbers[i] in numbers[i+1][:len(numbers[i])]:
            flag = False
            break
    if flag :
        print("YES")
    else:
        print("NO")