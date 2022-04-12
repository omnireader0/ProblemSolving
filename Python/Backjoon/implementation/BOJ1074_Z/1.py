n, r, c = map(int, input().split())
answer = 0
def solve(n, r, c):
    
    global answer
    if n == 0:
        return 
    
    size = 2**n
    l = size//2
    
    if r//l == 0 and c//l == 0:
        answer += l*l*0
        solve(n-1, r%l, c%l)
    elif r//l == 0 and c//l == 1:
        answer += l*l*1
        solve(n-1, r%l, c%l)
    elif r//l == 1 and c//l == 0:
        answer += l*l*2
        solve(n-1, r%l, c%l)
    else:
        answer += l*l*3
        solve(n-1, r%l, c%l)

solve(n, r, c)
print(answer)

'''
참고
https://cocoon1787.tistory.com/376

'''