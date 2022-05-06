'''
n이 최대 십만, s가 최대 1억이 주어진다.
연속된 수의 부분합을 구하기 위해 투포인터를 이용한다

'''
n, s = map(int, input().split())
arr = list(map(int, input().split()))
left, right = 0, 0
temp = 0
result = n+1

while True:
    if temp >= s:
        result = min(result, right-left)
        temp -= arr[left]
        left += 1
    
    elif right == n:
        break
    
    else:
        temp += arr[right]
        right += 1
if result == n+1:
    print(0)
else:
    print(result)
        
