import math
def solution(fees, records):
    answer = []
    car_info = dict()
    
    for r in records:
        temp = r.split(' ')
        temp[0] = int(temp[0][:2])*60 + int(temp[0][3:5])
        
        if not temp[1] in car_info:
            car_info[temp[1]] = [[temp[0], temp[2]]]
        else:
            car_info[temp[1]].append([temp[0], temp[2]])
            
    car_info = sorted(car_info.items())
    
    prefix_time = 0
    for key, values in car_info:
        if len(values) % 2 == 0:
            for j in range(len(values)):
                if values[j][1] == 'IN':
                    prefix_time -= values[j][0]
                else:
                    prefix_time += values[j][0]
            answer.append(prefix_time)
            prefix_time = 0
        else:
            for j in range(len(values)):
                if values[j][1] == 'IN':
                    prefix_time -= values[j][0]
                else:
                    prefix_time += values[j][0]
            answer.append(prefix_time+1439)
            prefix_time = 0
        
    final = []
    default_time, default_fee, unit_time, unit_fee = fees
    for i in answer:
        if i <= default_time:
            final.append(default_fee)
        else:
            final.append(default_fee + math.ceil((i-default_time)/unit_time)*unit_fee)
                
    return final