def solution(food_times, k):
    
    if sum(food_times) <= k:
        return -1
   
    length = len(food_times) # 음식 개수
    
    for i in range(length):
        food_times[i] = [food_times[i], i+1]
    
    food_time = sorted(food_times, key=lambda x : x[0])
    
    idx = 0 # 음식 순서
    previous_time = 0 # 남은 음식 시간
    
    while True:
        if (length-idx) * (food_time[idx][0] - previous_time) > k:
            break
        else:
            k -= (length - idx) * (food_time[idx][0] - previous_time)
            previous_time += food_time[idx][0] - previous_time # 현재 시간을 이전 시간으로 
            idx += 1 # 다음 음식 순서로
        #print(food_time)
    answer = sorted(food_time[idx:length], key= lambda x:x[1])
    return answer[k % len(answer)][1]