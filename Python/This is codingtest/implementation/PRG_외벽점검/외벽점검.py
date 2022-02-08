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