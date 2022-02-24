def check(answer):
    for x, y, equip in answer:
        if equip == 0: # 설치된 것이 기둥
            # 바닥 위, 보의 한쪽 끝부분 위, 다른 기둥 위 라면 ok
            if y ==0 or [x-1, y, 1] in answer or [x,y,1] in answer or [x,y -1,0] in answer:
                continue
            return False
        elif equip == 1: # 설치된 것이 보라면
            # 한쪽 끝 부분이 기둥 위, 혹은 양쪽 끝부분이 다른 보와 동시에 연결이면 ok
            if [x,y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y,1] in answer):
                continue
            return False
    return True
            
def solution(n, build_frame):
    answer = []
    for frame in build_frame: 
        x, y, equip, oper = frame
        if oper == 0: # 삭제
            answer.remove([x, y, equip])
            if not check(answer):
                answer.append([x, y, equip])
        elif oper == 1: # 설치
            answer.append([x, y, equip])
            if not check(answer):
                answer.remove([x,y, equip])
    return sorted(answer)