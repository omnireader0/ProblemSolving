
# 최대 공약수 gcd 활용
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def left_rotate(arr, d, n):
    
    for i in range(gcd(d, n)):    
        temp = arr[i] 
        j = i
        
        while True:
            
            k = j + d
            if k >= n:
                k = k - n
                
            if k == i:
                break
            
            arr[j] = arr[k]
            j = k
        
        arr[j] = temp
        
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
left_rotate(arr, 3, n)
print(arr) # [4, 5, 6, 7, 1, 2, 3]

'''
최대공약수 gcd를 이용해 집합을 나누어 여러 요소를 한꺼번에 이동시키는 것


j   k   0  1  2  3  4  5  6  7 
        a  b  c  d  e  f  g  h
0   3   d
3   6            g
6   1                     b
1   4      e
4   7               h
7   2                        c
2   5         f
5   0br                a
        d  e  f  g  h  a  b  c 
'''
      
