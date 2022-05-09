n = int(input())
arr = list(map(int, input().split()))
arr.sort()
min_ = 1e9
for i in range(n-3):
    for j in range(i+3, n):
        sum1 = arr[i] + arr[j]
        left, right = i+1, j-1
        while left < right:
            sum2 = arr[left] + arr[right]
            if abs(sum1-sum2) < min_:
                min_ = abs(sum1- sum2)
            if sum2 < sum1:
                left += 1
            elif sum2 > sum1:
                right -=1
            else:
                print(0)
                exit()
print(min_)   

'''
좀 더 고민해보기
'''