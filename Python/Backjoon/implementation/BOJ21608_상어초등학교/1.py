from collections import defaultdict
n = int(input())
graph = [[0]*n for _ in range(n)]
students = defaultdict()
number = []
for i in range(n**2):
    t = list(map(int, input().split()))
    students[t[0]] = t[1:]
    number.append(t[0])

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


# def solve(s):
    
    
# for i in number:
#     solve(i)
# '''

# '''