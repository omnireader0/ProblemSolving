import sys
input = sys.stdin.readline 
 
n = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))
max_, min_ = -1e9, 1e9

def dfs(value, cnt):
    global oper, max_, min_
    if cnt == n:
        temp = eval(value)
        max_ = max(temp, max_)
        min_ = min(temp, min_)
        return 
        
    if oper[0] > 0:
        oper[0] -= 1
        dfs(value + "+" + str(nums[cnt]), cnt+1)
        oper[0] += 1
    if oper[1] > 0:
        oper[1] -= 1
        dfs(value + "-" + str(nums[cnt]), cnt+1)
        oper[1] += 1
    if oper[2] > 0:
        oper[2] -= 1
        dfs(value + "*" + str(nums[cnt]), cnt+1)
        oper[2] += 1
    if oper[3] > 0:
        oper[3] -= 1
        dfs(value + "//" + str(nums[cnt]), cnt+1)
        oper[3] += 1

dfs(str(nums[0]), 1)
print(max_)
print(min_)

