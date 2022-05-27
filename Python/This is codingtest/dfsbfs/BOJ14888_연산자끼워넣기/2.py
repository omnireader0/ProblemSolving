n = int(input())
numbers = list(map(int, input().split()))
oper = list(map(int, input().split()))
max_ = -1e9 ; min_ = 1e9

def dfs(i, value):
    
    global max_, min_, oper
    
    if i == n:
        min_ = min(min_, value)
        max_ = max(max_, value)
        return
     
    if oper[0] > 0:
        oper[0] -= 1
        dfs(i+1, value + numbers[i])
        oper[0] += 1
        
    if oper[1] > 0:
        oper[1] -= 1
        dfs(i+1, value - numbers[i])
        oper[1] += 1

    if oper[2] > 0:
        oper[2] -= 1
        dfs(i+1, value * numbers[i])
        oper[2] += 1
    
    if oper[3] > 0:
        oper[3] -= 1
        dfs(i+1, int(value / numbers[i]))
        oper[3] += 1
        
dfs(1, numbers[0])
print(max_)
print(min_)
    
        
        
    
