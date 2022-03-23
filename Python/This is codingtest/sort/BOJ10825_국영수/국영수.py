n = int(input())
info = [input().split() for _ in range(n)]
info.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in info:
    print(i[0])
    
'''
접근 

간단한 정렬 문제, 람다를 이용해서 4 경우를 한꺼번에 정렬
'''