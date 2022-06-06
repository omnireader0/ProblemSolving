from copy import deepcopy

# 왼쪽으로 한 번 회전
def left_rotate_by_one(arr, n):
    
    arr = deepcopy(arr)
    temp = arr[0]
    for i in range(0, n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp
    return arr
    
# d만큼 회전
def left_rotate(arr, d, n):
    
    arr = deepcopy(arr)
    for i in range(0, d):
        arr = left_rotate_by_one(arr, n)
    return arr
        
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)

ans1 = left_rotate_by_one(arr, n)
ans2 = left_rotate(arr, 3, n)

print(ans1) # [2, 3, 4, 5, 6, 7, 1]
print(ans2) # [4, 5, 6, 7, 1, 2, 3]

'''
temp를 활용해서 첫번째 인덱스 값을 저장 후 arr[0]~arr[n-1]을 
각각 arr[1]~arr[n]의 값을 주고, arr[n]에 temp를 넣어준다.
'''