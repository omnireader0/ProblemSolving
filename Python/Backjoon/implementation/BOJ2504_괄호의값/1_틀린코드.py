s = input()
stack = []
result = 0
flag = True
temp = 1
for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')
        temp *= 2
    elif s[i] == '[':
        stack.append('[')
        temp *= 3
    elif s[i] == ')' :
        if stack:
            if s[i-1] == '(':
                result += temp
            stack.pop()
            temp //= 2
        elif not stack or stack[-1] != '(':
            flag = False
            break
    elif s[i] == ']':
        if stack:
            if s[i-1] == '[':
                result += temp
            stack.pop()
            temp //= 3
        elif not stack or stack[-1] != '[':
            flag = False
            break

if flag == True and not stack: 
    print(result)
else:
    print(0)
        
'''
43% 에서 자꾸 틀림..

(()([())])  -> 0 나와야함 , 근데 나는 28


분배 법칙을 사용해서 문제를 풀 수 있다. 
( ( ) [ [ ] ] ) 의 경우에 2x(2+3x3)으로 계산되는데, 
이는 결국 (2x2) + (2x3x3)과 같다. 
왼쪽 괄호가 나오면 temp에 2나 3을 곱한 뒤 스택에 push 하고, 
오른쪽 괄호가 나오면 temp를 2나 3으로 나눈 뒤 스택을 pop 한다. 
이때 ( ( ) [ [ ] ] ) 표시된 괄호처럼 괄호 값이
'( )' 또는 '[ ]'일 경우에는 temp 값을 나눠주기 전에 answer에 더한다. 


'''