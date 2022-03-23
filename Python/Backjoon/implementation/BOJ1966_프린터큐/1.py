from collections import deque
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())    
    q = deque(list(map(int, input().split())))
    cnt = 0
    while q:
        now = max(q)
        front = q.popleft()
        m -= 1
        
        if now == front:
            cnt += 1
            if m <0:
                print(cnt)
                break
        else:
            q.append(front)
            if m<0:
                m = len(q)-1
        
    
'''
풀이

중요도가 높은(숫자가 큰)문서가 가장 앞에 배치되어 있을 때 삭제되며,
나머지 문서들 중 중요도가 높은 문서가 하나라도 있으면 앞에 있는 문서 뒤에 재배치

우선 순위 큐 이용
now : 중요도 max
front : 큐의 맨 앞 원소
cnt : 삭제한 원소 개수 세기
m : 문서 포인터

큐에서 가장 중요도가 큰 값(now)가 front와 비교했을 때,
같다면 cnt 갱신하고, m(포인터)을 앞으로 한칸씩 당긴다.
이때 m이 0보다 작다면, 인쇄된 것이므로 break로 빠져나온다.  

'''