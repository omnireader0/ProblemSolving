r, c, k = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(3))

r = r-1
c = c-1

def sort(graph):
    temp = []
    idx = 0
    for width in graph:
        d = dict()
        for i in width:
            if i > 0:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
        # 개수 기준으로 오름차순 -> [(,),(,)...] 정렬하면 이런 모양임 
        a = sorted(list(zip(d.keys(), d.values())), key = lambda x : (x[1], x[0]))
        a = a[0:100]
        tmp = []
        for i in a:
            tmp.append(i[0])
            tmp.append(i[1])
        idx = max(idx, len(tmp))
        temp.append(tmp)
    # 0 패딩
    for j in range(len(temp)):
        while len(temp[j]) != idx:
            temp[j].append(0)
    return temp
            

cnt = 0
while cnt <= 100:
    
    width = len(graph[0])
    length = len(graph)
    
    if width > c and length > r and graph[r][c] == k:
        break
    
    # r 연산
    if length >= width:
        graph = sort(graph)
    else: 
        # c 연산
        graph = list(map(list, zip(*graph)))
        graph = sort(graph)
        graph = list(map(list, zip(*graph)))
        
    cnt += 1
    
if cnt == 101:
    cnt = -1
print(cnt)
    
    
'''
나중에 복습하기!! 
'''