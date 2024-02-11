def solution(num_list):
    answer = num_list
    multifly = 1
    add = 0
    
    for i in num_list:
        multifly *= i
        add += i
        
    if multifly < (add*add):
        return 1
    else:
        return 0
    
    return answer