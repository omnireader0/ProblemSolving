import sys
import copy
input = sys.stdin.readline
n = int(input())
for i in range(n):
    arr = [int(x) for x in input().split()]
    
    if i == 0:
        dp1 = copy.deepcopy(arr) # max
        dp2 = copy.deepcopy(arr) # min
    else:
        tmp1 = copy.deepcopy(dp1) # max
        tmp2 = copy.deepcopy(dp2) # min
        
        for j in range(3):
            if j == 0:
                dp1[j] = arr[j] + max(tmp1[j], tmp1[j+1])
                dp2[j] = arr[j] + min(tmp2[j], tmp2[j+1])
            elif j == 1:
                dp1[j] = arr[j] + max(tmp1[j-1], tmp1[j], tmp1[j+1])
                dp2[j] = arr[j] + min(tmp2[j-1], tmp2[j], tmp2[j+1])
            elif j == 2:
                dp1[j] = arr[j] + max(tmp1[j], tmp1[j-1])
                dp2[j] = arr[j] + min(tmp2[j], tmp2[j-1])
print(max(dp1), min(dp2))