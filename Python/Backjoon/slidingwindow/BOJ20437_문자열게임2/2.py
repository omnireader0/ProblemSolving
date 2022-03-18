def check():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    min_l = 10001
    max_l = 0
    flag = False
    for i in alpha:
        if i in s:
            if len(s.split(i)) > n:
                flag = True
                pos = -1
                match = []
                while True:
                    pos = s.find(i, pos+1)
                    if pos == -1:
                        break
                    match.append(pos)
                for i in range(0, len(match)-n+1):
                    end = (match[i+n-1] -match[i])
                    max_l = max(end, max_l)
                    min_l = min(end, min_l)
                
    if flag:
        return str(min_l+1)+" "+str(max_l+1)
    else:
        return -1
    
t =int(input())
for i in range(t):
    s = input()
    n = int(input())
    print(check())
    
    '''
    문자열 비교..이게 1번보다 빠르기는 함.. ㅋㅋ
    '''