from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
    max_diff, max_cnt = 0, {}
    
    for combi in combinations_with_replacement(range(11), n):
        cnt = Counter(combi)
        score1, score2 = 0, 0
        for i in range(1, 11):
            if info[10-i] < cnt[i]:
                score1 += i
            elif info[10-i]:
                score2 += i
                
        diff = score1 - score2
        if diff > max_diff:
            max_diff = diff
            max_cnt = cnt
    print(max_cnt)
    if max_diff > 0:
        answer = [0]*11
        for n in max_cnt:
            answer[10-n] = max_cnt[n]
        return answer
    else:
        return [-1]