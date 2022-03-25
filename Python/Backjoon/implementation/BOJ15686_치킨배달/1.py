from itertools import combinations
n, m = map(int, input().split())
cities = list(list(map(int, input().split())) for _ in range(n))

chickens = []
home = []
for i in range(n):
    for j in range(n):
        if cities[i][j] == 1:
            home.append([i,j])
        if cities[i][j] == 2:
            chickens.append([i,j])
        
chicken_combi = list(combinations(chickens, m))

answer = 1e9    
for combi in chicken_combi:
    result = 0
    for x, y in home:
        min_ = 100
        for a, b in combi:
            min_ = min(min_, abs(x-a)+abs(y-b))
        result += min_
    answer = min(result, answer)
    
print(answer)




'''
0 빈 칸
1 집
2 치킨집

'''