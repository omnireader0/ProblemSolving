def solution(board, skill):
    answer = 0
    arr = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    
    for type, r1, c1, r2, c2, degree in skill:
        # 누적합 기록
        if type == 2:
            arr[r1][c1] += degree
            arr[r1][c2+1] -= degree
            arr[r2+1][c1] -= degree
            arr[r2+1][c2+1] += degree
        else: 
            arr[r1][c1] -= degree
            arr[r1][c2+1] += degree
            arr[r2+1][c1] += degree
            arr[r2+1][c2+1] -= degree
    
    # 행 기준 누적합
    for i in range(len(arr)-1):
        for j in range(len(arr[0])-1):
            arr[i][j+1] += arr[i][j]
    
    # 열 기준 누적합
    for j in range(len(arr[0])-1):
        for i in range(len(arr)-1):
            arr[i+1][j] += arr[i][j]

    # 기존 배열 + 누적합
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += arr[i][j]
            if board[i][j] > 0:
                answer += 1
        
    return answer