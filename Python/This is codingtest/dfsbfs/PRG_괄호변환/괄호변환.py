def function(p):
    
    if len(p) == 0:
        return p
    
    u, v = '', ''
    cnt = 0
    
    for i in range(len(p)):
        cnt = cnt + 1 if p[i] == '(' else cnt - 1
        if cnt == 0:
            u = p[0:i+1]
            v = p[i+1:]
            break
    
    if correct_bracket(u):
        u += function(v)
        return u
    else:
        s = "(" + function(v) + ")"
        u = u[1:len(u)-1]
        s += reverse_bracket(u)
        return s
            
    
def correct_bracket(u):
    
    stack = []
    
    for i in u:
        if i == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    
    if len(stack) == 0:
        return True
    
def reverse_bracket(u):
    
    s = ''
    
    for i in u:
        s = s + ')' if i == '(' else s + '('
    return s
    
    
def solution(p):
    
    if len(p) == 0:
        return p
    return function(p)


print(solution("(()())()"))