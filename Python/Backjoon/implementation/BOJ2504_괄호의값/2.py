s = input()

stack1 = []
stack2 = []
temp = 1
result = 0
check = True

for i in range(len(s)):
    if s[i] == '(':
        stack1.append(s[i])
        temp *= 2
    elif s[i] == '[':
        stack2.append(s[i])
        temp *= 3
    elif s[i] == ')':
        if stack1:
            if s[i-1] == '(':
                result += temp
            stack1.pop()
            temp//=2
        else:
            check=False
            break
    elif s[i] ==']':
        if stack2:
            if s[i-1] == '[':
                result += temp
            stack2.pop()
            temp //=3
        else:
            check= False
            break
            
if check== True and not stack1 and not stack2:
    print(result)
else:
    print(0)
profile
Ýujiň ɧ