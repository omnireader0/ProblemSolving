import sys
input = sys.stdin.readline
n = int(input())
candy = list(list(input()) for _ in range(n))

def count():
    result = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if candy[i][j-1] == candy[i][j]:
                cnt += 1    
            else:
                result = max(result, cnt)
                cnt = 1
            result = max(result, cnt)
    
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if candy[j][i] == candy[j+1][i]:
                cnt += 1    
            else:
                result = max(result, cnt)
                cnt = 1
            result = max(result, cnt)
    return result    
        
maxl = 0
for i in range(n):
    for j in range(n-1):
    
        candy[i][j+1], candy[i][j] = candy[i][j], candy[i][j+1]
        maxl = max(maxl, count())
        candy[i][j+1], candy[i][j] = candy[i][j], candy[i][j+1]
        
        candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]
        maxl = max(maxl, count())
        candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]
    
print(maxl)

'''
인접한 서로 다른 두 사탕을 바꾸고, 행 또는 열에 대해 가장 긴 연속 부분을 구한다.
인접한 두 사탕은 좌우, 위 아래 모두 비교
좌우 바꿔서 가장 긴 연속 부분 계산
위아래 바꿔서 가장 긴 연속 부분 계산
'''