n = int(input())
triangle = []
for _ in range(n):
    tri = list(map(int , input().split()))
    triangle.append(tri)
for i in range(n-1, -1, -1):
    for j in range(0, i):
        triangle[i-1][j] += max(triangle[i][j], triangle[i][j+1])
print(triangle[0][0])
