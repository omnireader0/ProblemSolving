n, k = map(int, input().split())

for i in range(n//2+1):
    if (i+1)*((n-i)+1) == k:
        print("YES")
        break
else:
    print("NO")