'''
기둥 column  0
보 beam  1
''' 
# 보 설치
def build_beam(x, y, answer):
    # 바로 밑 또는 오른쪽 아래에 기둥이 있는 경우 또는 양쪽에 다른 보가 있는 경우
    if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
        answer.append([x, y, 1])
    return

# 기둥 설치
def build_column(x, y, answer):
    # 바닥이거나 또는 보의 한쪽(양방향) 끝부분  또는 밑에 기둥이 있는 경우
    if y==0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
        answer.append([x, y, 0])
    return

# 보 제거
def demolish_beam(x, y, answer):
    # 내 위의 기둥이 내가 사라지면 못버티는 경우
    if ([x, y, 0] in answer and [x, y-1, 0] not in answer and [x-1, y, 1] not in answer) or ([x+1, y, 0] in answer and [x+1, y-1, 0] not in answer and [x+1, y, 1] not in answer):
        return 
    # 내 왼쪽에 보가 있고, 왼쪽 보를 받쳐주는 기둥이 없으며, 나를 받쳐주는 기둥이 없는 경우
    elif [x-1, y, 1] in answer and [x-1, y-1, 0] not in answer and [x, y-1, 0] not in answer:
        return
    # 내 오른쪽에 보가 있는데 ~~
    elif [x+1, y, 1] in answer and [x+1, y-1, 0] not in answer and [x+2, y-1, 0] not in answer:
        return
    answer.remove([x, y, 1])
    return 

# 기둥 제거
def demolish_column(x, y, answer):
    # 내 왼쪽 위에 보가 있는데 버티지 못하는 경우
    if ([x-1, y+1, 1] in answer and [x-1, y, 0] not in answer and ([x-2, y+1, 1] not in answer or [x, y+1, 1] not in answer)):
        return
    # 내 오른쪽 위에 보가 있는데 버티지 못하는 경우
    elif ([x, y+1, 1] in answer and [x+1, y, 0] not in answer and ([x-1, y+1, 1] not in answer or [x+1, y+1, 1] not in answer)):
        return
    # 내 위에 기둥이 있는데 버티지 못하면
    elif ([x, y+1, 0] in answer and [x, y+1, 1] not in answer and [x-1, y+1, 1] not in answer):
            return
    answer.remove([x, y, 0])
    return


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, equip, oper = frame
        if oper:
            if equip:
                build_beam(x, y, answer)
            else:
                build_column(x, y, answer)
        else:
            if equip: 
                demolish_beam(x, y, answer)
            else:
                demolish_column(x, y, answer)
    return sorted(answer)

solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])