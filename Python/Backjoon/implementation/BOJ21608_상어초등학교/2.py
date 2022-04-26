import sys
input = sys.stdin.readline

n = int(input())
classroom = [ [0]*n for _ in range(n)]
likes = [[] for _ in range(n**2+1)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

for i in range(n**2):
    arr = list(map(int, input().split()))
    likes[arr[0]] = arr[1:]
    temp = []
    for j in range(n):
        for k in range(n):
            sum_like, sum_empty = 0, 0
            if classroom[j][k] != 0:
                continue
            for r in range(4):
                nx = j + dx[r]
                ny = k + dy[r]
                if 0 <= nx < n and  0 <= ny < n:
                    if classroom[nx][ny] in arr[1:]:
                        sum_like += 1
                    if classroom[nx][ny] == 0:
                        sum_empty += 1
            temp.append((sum_like, sum_empty, (j, k)))
    
    temp.sort(key=lambda x:(-x[0], -x[1], x[2]))
    classroom[temp[0][2][0]][temp[0][2][1]]= arr[0]

    
answer = 0
for i in range(n):
    for j in range(n):
        result = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and  0 <= ny < n and \
            classroom[nx][ny] in likes[classroom[i][j]]:
                result += 1
                continue
        if result != 0:
            answer += (10**(result-1))
print(answer)
            
