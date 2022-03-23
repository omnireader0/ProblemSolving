from collections import defaultdict
def solution(N, stages):
    answer = []
    l = len(stages)
    d = defaultdict(int)
    for i in stages:
        d[i] += 1
    
    for step in range(1, N+1):
        if d[step] == 0:
            answer.append((step, 0))
        else:
            answer.append((step, d[step]/l))
        l -= d[step]
    answer = sorted(answer, key = lambda x : x[1], reverse = True)
    answer = [i[0] for i in answer]
    return answer

'''
접근 : 구현 문제

풀이

1. 딕셔너리에 각 스테이지에 머물러 있는 사람의 수를 계산
2. 스테이지 단계를 1단계씩 증가시키면서 실패율 계산
    - 현재 단계에 있는 사람이 아무도 없다면, answer리스트에 (단계, 실패율 0) 삽입
    - 그렇지 않은 경우, answer에 (단계, 실패율) 삽입
    - 스테이지 도달한 유저만큼 길이를 조절해준다.
3. answer를 실패율이 높은 순으로 내림차순 정렬한다. 스테이지만 반환하도록 함
'''
