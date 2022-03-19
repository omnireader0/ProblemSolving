n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

result = [0]*(n+m)
i=0; j=0; k=0

while i<n or j<m:
    if j>= m or (i<n and arr1[i] < arr2[j]):
        result[k] = arr1[i]
        i += 1
    else:
        result[k] = arr2[j]
        j += 1
    k += 1
for i in result:
    print(i, end=' ')