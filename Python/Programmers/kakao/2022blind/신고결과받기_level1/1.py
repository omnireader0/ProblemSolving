def solution(id_list, report, k):
    l = len(id_list)
    answer = [0]*(l)
    report_id = [[] for _ in range(l)] # 각 유저-신고한id 매핑 정보
    report_cnt = [0]*(l) # 신고 횟수 정보
    suspend_id = '' # 정지 아이디
    
    for re in report:
        r = re.split(' ')
        a = r[0]
        b = r[1]
        idx = id_list.index(a)
    
        if b not in report_id[idx]:
            report_cnt[id_list.index(b)] += 1
        report_id[idx].append(b)

    
    for i in range(l):
        if report_cnt[i] >= k:
            suspend_id = id_list[i]
            for j in range(l):
                if suspend_id in report_id[j]:
                    answer[j] += 1
        
    return answer


'''
report에서 하나씩 데이터 입력 받고,
각 유저-신고한id를 매핑하며, 신고당한 경우 카운트(단, 동일인에게 신고당한 적 없다면..)

신고 당한 횟수가 k이상이라면, 그 유저를 리스트에 담고,
각 유저-신고한 id를 매핑 정보에서 처리 결과 메일을 보낼 것인지 확인
'''