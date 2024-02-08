def solution(num_list):
    answer = 0
    num1 = "" #짝수
    num2 = "" #홀수
    
    for i in num_list:
        if i % 2 == 0 :
            num1 += str(i)
        else:
            num2 += str(i)
            
    answer = int(num1) + int(num2)
    
    return answer