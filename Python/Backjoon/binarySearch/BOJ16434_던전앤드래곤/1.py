import sys
import math

n, m = map(int, input().split())
room = []
for _ in range(n):
    data = list(map(int, input().split()))
    room.append(data)
    
    
left, right = 1, int(1e18)
answer = 0
while left <= right:
    mid = (left + right) // 2 # 최대 생명력
    
    # 용사 입장 시 생명력, 공격력 
    vitality, attack = mid, m
    for i in room:
        if i[0] == 1: # 몬스터 등장
            # 몬스터 생명력 갱신, 공격의 순서 : 용사 -> 몬 이므로 
            # 몬스터는 용사의 공격 기회보다 1번 더 적은 상태에서 공격을 할 수 있음
            vitality -= (math.ceil(i[2]/attack)-1) * i[1]
            if vitality <= 0:
                break
        else: # 포션
            attack += i[1]
            vitality += i[2]
            vitality = min(mid, vitality)
    
    # 최대 생명력이 mid일때 용을 쓰러트릴 수 있는가
    if vitality > 0:
        right = mid - 1
        answer = mid # 결정문제의 답은 lo의 다음 칸이 hi일 때이므로 여기서 해 구하기 
    else: left = mid + 1
    
print(answer)
    
'''
결정 문제 : 최대 생명력이 mid일 때 용을 쓰러트릴 수 있는가
방의 개수 123456, 용사 공격력 10^6 용사 생명력 10^6
lo=0 , hi= 1e18 (n개의 방에서 1e6의 공격력으로 1e6번 공격당함)
'''