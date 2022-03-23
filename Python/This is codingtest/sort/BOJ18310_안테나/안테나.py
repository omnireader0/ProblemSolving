n = int(input())
data = sorted(list(map(int, input().split())))
print(data[(n-1)//2])

'''
접근 

집이 위치한 곳을 정렬하여 중간에 위치한 집을 찾으면 최솟값 보장
'''