n, k = map(int, input().split())
s = list(map(int, input().split()))
d = list(map(int, input().split()))
p = [0]*len(s)

while True:
    if k == 0:
        break
    for i in range(len(d)):
        idx = d[i]-1
        p[idx] = s[i]
    s[:] = p[:]
    k -= 1
for i in p:
    print(i, end=' ')

    