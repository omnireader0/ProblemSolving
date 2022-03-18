from collections import defaultdict
import sys
input = sys.stdin.readline
n, d, k, c = map(int, input().split()) # 접시의 수, 초밥 가짓수, 연속해서 먹는 접시 수, 쿠폰 번호
sushi = list(int(input()) for _ in range(n))
sushi += sushi[:k-1]
sushi_set = defaultdict(int)

sushi_set[c] += 1

start = 0
end = 0
max_cnt = 0
for end in range(len(sushi)):
    sushi_set[sushi[end]] += 1
    
    if end >= k-1:
        max_cnt = max(max_cnt, len(sushi_set))
        sushi_set[sushi[start]] -= 1
        
        if sushi_set[sushi[start]] == 0:
            del sushi_set[sushi[start]]
        start += 1
        
print(max_cnt)

'''
슬라이딩 윈도우로 O(N)에 해결 가능
초밥은 회전하므로 이것을 일렬로 표현 (sushi += sushi[:k-1])
이때 윈도우는 딕셔너리로 구현하여, 연산을 빠르게 처리하도록 했음

풀이
1. 딕셔너리에 쿠폰 초밥 미리 추가
2. 반목문을 통해 초밥 앞에서 하나씩 꺼내서 셋트에 추가
3. 셋트 사이즈가 K개보다 커지면 맨 앞에 위치한 초밥을 하나씩 제거한다.
그리고 초밥 종류가 다양한 경우를 저장한다.
'''