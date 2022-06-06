'''
회전시키는 수에 대해 구간을 나누어 reverse로 구현하는 방법
d = 2이면
1,2 / 3,4,5,6,7로 구간을 나눈다.
첫번째 구간 reverse -> 2,1
두번째 구간 reverse -> 7,6,5,4,3
합치기 -> 2,1,7,6,5,4,3
합친 배열을 reverse -> 3,4,5,6,7,1,2


'''
from copy import deepcopy

# swap을 활용한 reverse 구현
def reverse_arr(arr, start, end):
    
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# d로 나눠서 역전 알고리즘 수행
def rotate_left(arr, d, n):
    
    arr = deepcopy(arr)
    reverse_arr(arr, 0, d-1)
    reverse_arr(arr, d, n-1)
	reverse_arr(arr, 0, n-1)
     
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
rotate_left(arr, 3, n)