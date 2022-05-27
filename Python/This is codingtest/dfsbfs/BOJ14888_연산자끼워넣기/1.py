n = int(input())
numbers = list(map(int, input().split()))
oper = list(map(int, input().split()))
answer = []

def calculate(i, res, now):
    if i == 0:
        return res + now
    elif i == 1:
        return res - now
    elif i == 2:
        return res * now
    else:
        return int(res / now)
    
def dfs(cnt, res):
    global oper
    result = 0
    
    if cnt == n:
        answer.append(res)
        return

    for i in range(4):
        if oper[i] > 0:
            result = calculate(i, res, numbers[cnt])
            print(oper)
            oper[i] -= 1
            dfs(cnt+1, result)
            oper[i] += 1
 
dfs(1, numbers[0])
print(max(answer))
print(min(answer))

'''
1. 접근

연산의 최대 개수가 10개 이므로 가능한 경우의 수 10!이며(2초안에 해결 가능), 
10!은 제한 시간 안에 해결 가능하므로 재귀를 이용한 탐색 이용

재귀는 백트래킹의 개념을 dfs를 이용하여 정의했음
(포인트 : 방문이 끝나고 돌아오면 방문했던 노드를 방문하지 않은 상태로 변경하는 것을 고려)

2. 검증
시간복잡도 : O(4^N)
DFS O(V+E) -> O(11+4^10), DFS 한 번 돌릴 때 마다 4 분기함
공간복잡도 : O(15+10!)
n변수:1, numbers리스트: n, oper리스트: 4, answer리스트: n!보다 작음
(n이 최대 11이고, 10이라고 가정)
(사실은 oper가 4개이기 때문에, 연산의 개수가 10개더라도, 1 3 3 3 / 2 2 3 3 ...10!보다 작을 것임)

3. 풀이
numbers는 연산할 숫자가 담긴 리스트
oper는 각 연산 기호의 가용 횟수 리스트

calculate(i, res, now)
i는 부호 인덱스, res는 연산 결과, now는 피연산자
연산 결과에 피연산자를 연산한 결과를 리턴해 줌

dfs(cnt, res)
"cnt는 연산할 숫자(피연산자)의 인덱스, res는 연산의 결과"를 매개변수로 담아서 정의
cnt가 n과 같다면 더이상 피연산자가 없으므로 종료 조건 작성
반복문을 통해 (+, -, *, %) 각각에 대해 조건에 맞다면 calculate
oper에서 연산한 부호의 가용 횟수를 1개 뺴주고, dfs를 돌림
dfs 결과 연산이 끝났다면, 연산 처리했던 oper를 되돌린다. 


4. 처음 실패했던 이유
~~~
else:
        return int(res / now)
        # return res // now
~~~

1) print(-5//2) = -3
2) print(int(-5/2)) = -2
 
문제에서 2의 결과가 나와야 함

나눗셈은 정수 나눗셈으로 몫만 취한다.
음수를 양수로 나눌 때 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다.
-5/2 = -(5/2) = -2.5 양수로 바꿔서 계산하고 앞에 부호 붙이기
int(-2.5) = -2 몫만 가져옴
'''
