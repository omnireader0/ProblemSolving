import math

def convert(n, k):
    result = ''
    while n > 0:
        n, mod = divmod(n,k)
        result += str(mod)
    return result[::-1]

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True        

def solution(n, k):
    trans = convert(n,k)
    trans = trans.split('0')
    remove = {'', '1'}
    trans = [i for i in trans if i not in remove]
    
    cnt = 0
    for t in trans:
        if is_prime(int(t)):
            cnt += 1
    return cnt

# sol 2
# def solution(n, k):
#     trans = convert(n,k)
#     trans = trans.split('0')
#     remove = {'', '1'}
#     trans = [i for i in trans if i not in remove]
    
#     cnt = 0
#     for t in trans:
#         flag = True
#         t = int(t)
#         for i in range(2, int(math.sqrt(t))+1):
#             if t % i == 0:
#                 flag = False
#         if flag == True:
#             cnt += 1
#     return cnt