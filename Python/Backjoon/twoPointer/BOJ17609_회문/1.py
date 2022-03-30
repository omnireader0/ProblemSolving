t = int(input())

def similar_palindrom(s, left, right):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def palindrom(s, left, right):
    # 완전 회문
    if s == s[::-1]:
        return 0
    else:
        while left < right:
            if s[left] != s[right]:
                temp1 = similar_palindrom(s, left+1, right)
                temp2 = similar_palindrom(s, left, right-1)
                
                if temp1 or temp2:
                    return 1
                else:
                    return 2
            else:
                left += 1
                right -= 1
         
for i in range(t):
    s = input()
    left, right = 0, len(s)-1
    print(palindrom(s, left, right))
        
'''
1. 풀이

회문 함수
- if 완전 회문이라면
    리턴 1
- else
    - 유사 회문 가능한지 체크
    - 이때, 유사 회문 함수 이용
    - 가능하면 리턴1, 가능하지 않으면 리턴2

유사 회문 함수
- 투포인터로 비교하면 됨
- 리턴값 true or false

반례
1
abca
0
'''