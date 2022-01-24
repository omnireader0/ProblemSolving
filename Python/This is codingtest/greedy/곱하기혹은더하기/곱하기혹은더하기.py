s = input()

answer = int(s[0])

for i in s[1:]:
    i = int(i)
    if i<=1 or answer<=1:
        answer += i
    else:
        answer *= i
        
print(answer)

