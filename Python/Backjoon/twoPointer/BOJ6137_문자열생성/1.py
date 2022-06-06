n = int(input())
s = ''
for _ in range(n):
    s += input()

t = ''
left = 0
right = n-1
while left <= right:
    if s[left] > s[right]:
        t += s[right]
        right -= 1
    
    elif s[left] < s[right]:
        t += s[left]
        left += 1
    
    else:
        ll, rr  = left+1, right-1
        flag = False
        while ll <= rr:
            if s[ll] < s[rr]:
                t += s[left]
                left += 1
                flag = True
                break
            elif s[ll] > s[rr]:
                t += s[right]
                right -= 1
                flag = True
                break
            ll += 1
            rr -= 1
        if not flag:
            t += s[left]
            left += 1
                
    
print(t)
cnt = 0
for i in t:
    print(i, end='')
    cnt += 1
    if cnt % 80 == 0:
        print() 