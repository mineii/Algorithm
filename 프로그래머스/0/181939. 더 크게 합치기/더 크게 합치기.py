def solution(a, b):
    tmp1 = int(str(a) + str(b))
    tmp2 = int(str(b) + str(a))
    
    if tmp1 > tmp2:
        return tmp1
    elif tmp1 < tmp2:
        return tmp2
    else:
        return tmp1