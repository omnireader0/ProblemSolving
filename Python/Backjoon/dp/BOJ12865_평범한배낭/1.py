n, k = map(int, input().split())
item=[[0,0]]
backpack = [[0]*(k+1) for _ in range(n+1)]

for _ in range(n):
    item.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, k+1):
        w = item[i][0] # 무게
        v = item[i][1] # 가치
        # i 번째에 무게 더 담을 수 없는 경우
        # 현재 물건이 현재 가방 무게보다 작다면 [이전물건][같은무게]를 저장
        if j < w:
            backpack[i][j] = backpack[i-1][j] 
        # i번째에 더 담을 수 있는 경우
        # 현재물건가치+남은무게를 채울 수 있는 가치 최댓값 vs 다른 물건으로 채우는 최댓값
        else:
            backpack[i][j] = max(v+backpack[i-1][j-w], backpack[i-1][j])
print(backpack[n][k])