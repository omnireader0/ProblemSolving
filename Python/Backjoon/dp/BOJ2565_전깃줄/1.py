n = int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
arr.sort()

# LIS

arr_b = [arr[i][1] for i in range(len(arr))]

length = [0]*n
for i in range(n):
    length[i] = 1
    for j in range(i):
        if arr_b[j] < arr_b[i]:
            length[i] = max(length[i], length[j]+1)

print(n - max(length))