s = input()
answer = []
number = 0
for i in s:
    if i.isalpha():
        answer.append(i)
    else:
        number += int(i)
answer.sort()
if number != 0:
    answer.append(str(number))
print(''.join(answer))
