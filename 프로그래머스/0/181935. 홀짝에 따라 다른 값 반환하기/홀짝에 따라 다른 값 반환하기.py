def solution(n):
    num = 0
    if n % 2 == 1:
        for i in range(1, n+1):
            if i % 2 == 1:
                num += i
                
    else:
        for i in range(1, n+1):
            if i % 2 == 0:
                num += int(i*i)
                
    return num