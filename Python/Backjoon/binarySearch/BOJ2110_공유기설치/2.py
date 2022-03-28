n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

def binarysearch(left, right):
    mid = (left + right) //2
    
    if left > right:
        print(mid)
        return
    
    cnt = 1
    pre = arr[0]
    for i in range(1, n):
        if arr[i] >= pre + mid:
            cnt += 1
            pre = arr[i]
            
    if cnt >= m:
        binarysearch(mid+1, right)
    elif cnt < m:
        binarysearch(left, mid-1)
        
binarysearch(1, arr[-1]-arr[0]) # gap을 1 , max


'''
1. 접근
좌표가 최대 10억, logN으로 연산하겠다는 아이디어 -> 이분탐색(파라메트릭 서치)

- 이분탐색 : 정렬된 배열에서 target 값이 있다면 리턴
- 파라메트릭 서치 : target과 일치하는 값이 없을 수도 있다는 것을 가정하며,
범위 내에서 최적값을 찾는 알고리즘
    - 푸는 법 : 최적화문제를 yes or no(결정문제)로 풀기
    - 최적화 문제 : 가장 좋은 답 찾기
    - 결정 문제 :  ‘답 x가 존재하는가?’ 대신 ‘x 또는 그보다 좋은 답이 있는가?’
    - 결정문제를 내부적으로 이용하는 이분탐색 알고리즘 작성해서 풀자!

2. 풀이
gap -> 최소 1, 최대 : 가장 큰 차이
1) gap의 범위를 비교구간으로 하여, mid(중간에 해당하는 갭)를 구한다.
2) 인접한 두 공유기 사이가 mid보다 크다면 공유기 설치
3) 설치한 공유기의 개수가 m보다 많다면, 인접한 두 공유기 사이의 거리를 증가시킨다.
더 큰 값에 대해서도 m개의 공유기를 설치할 수 있는지 체크한다.

-> 단순히 구하고자 하는 값이 아닌 최대 거리를 찾겠다 : 파라메트릭 서치 
'''