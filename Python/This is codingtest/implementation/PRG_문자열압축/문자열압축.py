def solution(s):
    answer = len(s)
    
    for i in range(1, len(s)//2+1):
        comp = ""
        cnt = 1
        prev = s[:i]
        for j in range(i, len(s)+i, i):
            if s[j:j+i] == prev:
                cnt += 1
            else:
                if cnt == 1:
                    comp += prev
                else:
                    comp += str(cnt) + prev
                prev = s[j:j+i]
                cnt = 1
        answer = min(answer, len(comp))
    return answer
                
