n, k = map(int, input().split())
arr = list(map(int, input().split()))
start = 0
curr_sum = 0
max_sum = -1e9

for i, val in enumerate(arr):
    curr_sum += val
    
    if i-start+1 == k:
        max_sum = max(max_sum, curr_sum)
        curr_sum -= arr[start]
        start += 1
        
print(max_sum)