from collections import defaultdict
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    s = input()
    k = int(input())
    
    d = defaultdict(list)
    for i in range(len(s)):
        if s.count(s[i]) >= k:
            d[s[i]].append(i)
    
    if len(d) == 0:
        print(-1)
        continue
    
    min_ = 10001
    max_ = 0
    
    for i in d.values():
        for j in range(len(i)-k+1):
            result = i[j+k-1] - i[j] + 1

            if result < min_:
                min_ = result
            if result > max_:
                max_ = result
    
    print(min_, max_)


'''
슬라이딩 윈도우로 해결
딕셔너리에 k번이상 등장하는 문자만 넣고, 딕셔너리에서 값 꺼내서 최솟값, 최댓값 구함
'''