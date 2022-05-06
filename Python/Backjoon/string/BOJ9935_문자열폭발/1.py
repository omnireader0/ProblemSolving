'''
문자열 길이 최대 백만, 폭발 문자열 길이 최대 36
일일이 비교하면 최악의 경우 3600백만 연산

그래서 스택을 이용해서 문자열의 길이만큼만 연산하는 방법을 선택
스택에 s를 집어 넣고, 접미사가 k와 같다면 폭발
'''

s = input() # 문자열
k = input() # 폭발문자열
stack = []
last_k = k[-1]
n = len(k)
for i in range(len(s)):
    stack.append(s[i])
    if s[i] == last_k and "".join(stack[-n:]) == k:
        del stack[-n:]
if stack:
    print("".join(stack))
else:
    print('FRULA')