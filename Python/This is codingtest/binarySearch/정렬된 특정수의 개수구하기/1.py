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

'''
1. 접근
logN으로 설계, 오름차순 데이터 -> 이분탐색
이분탐색의 컨셉은 정렬된 리스트에서 탐색 범위 절반씩 좁혀 탐색하므로 logN에 비례
값이 x인 원소의 개수를 구해야하는데,
앞에서 x를 찾는 함수와 뒤에 위치한 x를 찾는 함수로 인덱스를 구한다!

2. 시간복잡도
logN * 2 ->  logN

3. 풀이

first 함수

mid : 비교 구간의 중간에 위치한 인덱스
리스트의 mid에 위치한 값이 target보다 크거나 같다면 mid 앞 탐색, 그게 아니면 mid 뒤 탐색

여기서 x 값 가지는 원소 중 가장 왼쪽에 있는 경우를 리턴해야 하는데,
가장 왼쪽에 있는 경우는 (x가 인덱스 0에 위치하거나, target값이 array[mid-1]보다 큰 경우에) 
array[mid]==target이라면 가장 왼쪽에 있는 경우라고 볼 수 있다.

start > end인 경우 더이상 비교할 수 없으므로 조건문 처리

'''