t = int(input())

def palindrom(s):
    left, right, cnt = 0, len(s)-1,  0
   
    while left < right:
        if s[left] != s[right]:
            
            # 왼쪽 삭제하고 비교하기
            l, r = left, right
            l += 1
            
            if l == r:
                if cnt == 0:# abca 인 경우, b와 c의 포인터가 같아지면 아래 비교를 못함
                    return 1
                elif cnt == 1:
                    return 2
            
            while l < r:
                if s[l] != s[r]:
                    cnt += 1
                    break
                l += 1
                r -= 1
                
            # 오른쪽 삭제하고 비교하기
            l, r = left, right
            r -= 1
            
            
            
            while l < r:
                if s[l] != s[r]:
                    cnt += 1
                    break
                l += 1
                r -= 1
                
            return cnt
            
        left += 1
        right -= 1
        
    return cnt
         
for i in range(t):
    s = input()
    print(palindrom(s))
        
        
'''
1. 회문 함수
- if 완전 회문인가?
- else
    - 

3. 문자열


4. 반례
1
abca
0
'''