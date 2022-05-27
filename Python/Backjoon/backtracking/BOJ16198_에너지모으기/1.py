# E = 0
# def getEnerge(N, e, wn) :
#     if N == 2:
#         global E
#         E = max(E,e) 
#     else :
#         for x in range(1, N-1) :
#             e += ( wn[x-1] * wn[x+1] )
#             getEnerge(N-1,e,wn[:x]+wn[x+1:])
#             e -= ( wn[x-1] * wn[x+1] )

# N = int(input())
# arr = list(map(int, input().split()))

# getEnerge(N,0,arr)
# print(E)

'''
접근

N과 에너지 구슬의 무게가 주어졌을 때, 모을 수 있는 에너지 양의 최댓값을 구해야 한다.
어떤 구슬을 먼저 선택하냐에 따라 에너지양의 값은 매번 달라진다.
N이 최대 10개 이므로, 모든 경우의 수를 탐색(재귀)하되, 
N이 2가 되면, 종료 조건이 된다.
N과 M(1)과 비슷한 로직으로 해결할 수 있다.


1. 처음과 마지막을 제외한 구슬 1개를 고르고
2. 고른 구슬의 앞뒤 구슬을 통해 에너지를 모은다.
3. 고른 구슬 감소시키고, 1~2를 반복한다.
이때, 구슬의 개수가 2개가 되면, 종료 조건이 된다.(1,2를 반복X)
 
'''

n = int(input())
arr = list(map(int, input().split()))
energy = 0

def dfs(n, e, arr):

    global energy
    if n == 2:
        energy = max(energy, e)

    for i in range(1, n-1):
        e += arr[i-1]*arr[i+1]
        temp = arr[:i] + arr[i+1:]
        dfs(n-1, e, temp)
        e -= arr[i-1]*arr[i+1]

dfs(n, 0, arr)
print(energy)
