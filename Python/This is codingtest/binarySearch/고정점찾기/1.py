def binary_search(array, start, end):
    while start <= end:
        mid = (start + end)//2
        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return None
n = int(input())
array = list(map(int, input().split()))
answer = binary_search(array, 0, n-1)
if answer == None:
    print(-1)
else:
    print(answer)

'''
1. 접근 
logN으로 설계, 오름차순 -> 이분탐색

2. 시간복잡도
lonN

3. 풀이
찾고자 하는 값이 비교구간의 중간 위치한 값과 동일하면 리턴
'''
