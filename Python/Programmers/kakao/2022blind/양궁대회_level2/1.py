from collections import deque

def bfs(n, info):
    result = []
    q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
    max_diff = 0
    
    while q:
        focus, arrow = q.popleft() 
        
        if sum(arrow) == n: # 종료조건1 : 화살 다 쏜 경우
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            
            if apeach < lion: # 라이언 승
                diff = lion - apeach
                if max_diff > diff:
                    continue
                if max_diff < diff:
                    max_diff = diff
                    result.clear()
                    
                result.append(arrow) # 최대 점수차 나는 화살 저장
                    
        elif sum(arrow) > n: # 종료 조건2 : 화살 덜 쏜 경우
            continue
        
        elif focus == 10: # 종료 조건3: 화살 덜 쏜 경우
            tmp = arrow.copy()
            tmp[focus] = n - sum(tmp)
            q.append((-1, tmp))
            
        # 승률 내는 법 : 어피치보다 1발 더 쏘기 vs 화살 아끼기
        else: # 화살 쏘기
            tmp = arrow.copy()
            tmp[focus] = info[focus] + 1
            q.append((focus+1, tmp))  # 어피치보다 1발 많이 쏘기
            tmp2 = arrow.copy()
            tmp2[focus] = 0
            q.append((focus+1, tmp2))  # 0발 쏘기
    return result
    
def solution(n, info):
    answer = bfs(n, info)
    
    if not answer:
        return [-1]
    elif len(answer) == 1:
        return answer[0]
    else:
        return answer[-1]