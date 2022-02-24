'''
완전 탐색으로 해결
1. 외벽이 원형 -> 일자로 만들기 위해 2배로 늘림
2. 친구를 나열하는 경우를 순열로 구하기
3. 2번 각각의 경우에 대해 취약 지점 방문가능한지 모두 체크
- 한명씩 투입하면서, 해당 친구가 점검할 수 있는 마지막 위치를 구하고, 점검을 다 못하는 경우 새친구를 투입한다.
- 더이상 투입 불가라면 조건문 탈출하고, 그게 아니라면 마지막 위치를 갱신한다.
'''
from itertools import permutations

def solution(n, weak, dist):
    # 원형을 일자로 변경 -> 길이 2배로
    weak_length = len(weak)
    weak += [i+n for i in weak]
    answer = 9
    for start in range(weak_length):
        # 친구 나열하는 경우를 순열로 
        for people in list(permutations(dist, len(dist))):
            cnt = 1 # 1명 투입
            last_location = weak[start] + people[cnt-1]
            for idx in range(start, start+weak_length):
                # 점검을 다 못하는 경우
                if last_location < weak[idx]:
                    cnt += 1 # 새 친구 투입
                    if cnt > len(dist): # 더이상 투입 불가
                        break
                    last_location = weak[idx] + people[cnt-1]
            answer = min(answer, cnt)
    if answer > len(dist):
        return -1
    return answer