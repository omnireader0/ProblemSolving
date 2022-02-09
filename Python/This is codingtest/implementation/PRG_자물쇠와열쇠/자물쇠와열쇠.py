def rotate_a_matrix_by_90_degree(t):
    n = len(t) # 행
    m = len(t[0]) # 열
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = t[i][j]
    return result
    
# 자물쇠의 중간 부분 모두 1인지 검사 - 더했을 때 모두 1이면 ok
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True
    
    
def solution(key, lock):
    n = len(lock)
    m = len(key)  
    # 자물쇠 크기를 기존의 3배로 변환
    new_lock = [[0]* (n*3) for _ in range(n*3)]
    # 새로운 자물쇠 중간에 자물쇠 배치
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
            
    # 4가지 방향에 대해 확인
    for  _ in range(4):
        key = rotate_a_matrix_by_90_degree(key) # 열쇠 회전
        for x in range(n*2):
            for y in range(n*2):
                #  자물쇠에 열쇠 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock):
                    return True
                # 자물쇠에서 열쇠 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False 