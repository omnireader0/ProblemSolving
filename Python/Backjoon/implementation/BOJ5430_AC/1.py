from collections import deque
import sys
input = sys.stdin.readline
t = int(input())

for i in range(t):
    oper = input().rstrip()
    n = int(input())
    arr = input().rstrip()[1:-1].split(',')
    q = deque(arr)
    cnt = 0
    flag = True
    if n == 0 :
        q = deque()
    for j in range(len(oper)):
        if oper[j] == 'R':
            cnt += 1
        else: 
            if len(q) > 0:
                if cnt % 2 != 0:
                    q.pop()
                else:
                    q.popleft()
            else:
                flag = False
                break
        
    if cnt % 2 != 0:
        q.reverse()
        
    if flag : print('[' + ",".join(q) +"]")
    else: print('error')

'''
- r은 역순 정렬인데, 이것을 매번하면 시간초과 -> r의 개수 홀짝 따져서 pop
- r의 개수가 홀수라면, 마지막에 역순 정렬해줌
- n이 0인 경우, 큐에 deque([' '])이 아니라 deque(['']) 담아줘야 함
'''
