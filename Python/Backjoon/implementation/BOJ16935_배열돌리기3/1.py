n, m, r = map(int,input().split())
graph = list(list(map(int, input().split())) for _ in range(n))
count = list(map(int, input().split()))

def func1(): # 상하 반전
    global graph
    temp = [[0]*m for _ in range(n)]
    temp = graph[::-1]
    return temp

def func2(): # 좌우 반전
    global graph
    temp = [[0]*m for _ in range(n)]
    for i in range(n):
        temp[i] = graph[i][::-1]
    return temp

def func3(): # 오른쪽 90도
    global graph, n, m
    temp = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            temp[i][j] = graph[n-j-1][i]
    return temp

def func4(): # 왼쪽 90도
    global graph, n, m
    temp = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            temp[i][j] = graph[j][m-i-1]
    return temp

def func5(): # 시계방향
    global graph, n, m
    temp = [[0]*m for _ in range(n)]
    nn = n//2
    mm = m//2
    for i in range(n):
        for j in range(m):
            if 0<=i<nn and 0<=j<mm:
                temp[i][j] = graph[i + nn][j]
            elif (0 <= i < nn and j >= mm):
                temp[i][j] = graph[i][j - mm]
            elif (i >= nn and j >= mm):
                temp[i][j] = graph[i-nn][j]
            elif (i >= nn and 0 <= j < mm):
                temp[i][j] = graph[i][j+mm]
    return temp
    
def func6():
    global graph, n, m
    temp = [[0]*m for _ in range(n)]
    nn = n//2
    mm = m//2
    for i in range(n):
        for j in range(m):
            if 0<=i < nn and 0 <=j <mm:
                temp[i][j] = graph[i][j+mm]
            elif 0 <= i<nn and j>= mm:
                temp[i][j] = graph[i+nn][j]
            elif i>= nn and j>=mm:
                temp[i][j] = graph[i][j-mm]
            elif i>= nn and  0<= j<mm:
                temp[i][j] = graph[i-nn][j]
    return temp

for i in count:
    if i == 1:
        graph = func1()
    elif i == 2:
        graph = func2()
    elif i == 3:
        graph = func3()
        n, m = m, n
    elif i == 4:
        graph = func4()
        n, m = m, n
    elif i == 5:
        graph = func5()
    elif i == 6:
        graph = func6()
        
for i in graph:
    for j in i:
        print(j, end=" ")
    print()