'''
리프노드의 개수를 구해야 한다.
리프노드란 자식 노드가 없는 노드를 말한다.
트리를 구성할 때, 부모노드-자식노드 정보를 입력하는데,
삭제할 노드와 루트 노드는 제외한다.
그리고, 트리를 dfs 순회하면서, 리프노드(dfs 순회할 수 없는)를 발견하면 개수를 센다.
'''
n = int(input())
data = list(map(int, input().split()))
tree = [[] for _ in range(n)]
delete_node = int(input())

cnt = 0
def dfs(x):
    global cnt
    if not tree[x]: # 자식 노드 없다면 리프노드

        cnt += 1
        return 
    for i in tree[x]: # 자식 노드 있으면 dfs 순회
        dfs(i)

for i in range(n):
    if data[i] == -1:
        root = i 
        continue
    elif i == delete_node:
        continue
    
    tree[data[i]].append(i) # 부모 노드와 자식 노드
    
if root != delete_node:
    dfs(root)
print(cnt)