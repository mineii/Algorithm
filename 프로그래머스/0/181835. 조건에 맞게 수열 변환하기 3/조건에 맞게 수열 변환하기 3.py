def solution(arr, k):
    answer = []
    
    for item in arr :
        if k % 2 == 1:
            answer.append(item * k)
        else:
            answer.append(item + k)
            
    return answer