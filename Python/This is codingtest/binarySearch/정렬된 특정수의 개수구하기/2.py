from bisect import bisect_left, bisect_right

n, x = map(int, input().split()) 
array = list(map(int, input().split()))

first = bisect_left(array, x)
last = bisect_right(array, x)

print(last-first) if first != 0 else print(-1)