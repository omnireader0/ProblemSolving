def first(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if (mid == 0 or target > array[mid-1]) and array[mid] == target:
        return mid
    elif array[mid] >= target: # mid보다 값이 작거나 같은 경우 왼쪽 탐색
        return first(array, target, start, mid-1)
    else: 
        return first(array, target, mid+1, end)

def last(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if (mid==n-1 or target < array[mid+1]) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return last(array, target, start, mid-1)
    else: # mid 보다 값이 크거나 같은 경우 오른쪽 탐색 
        return last(array, target, mid+1, end)
    
n, x = map(int, input().split())
array = list(map(int, input().split()))
a = first(array, x, 0, n-1)
b = last(array, x, 0, n-1)
print(b-a+1) if a != None else print(-1)