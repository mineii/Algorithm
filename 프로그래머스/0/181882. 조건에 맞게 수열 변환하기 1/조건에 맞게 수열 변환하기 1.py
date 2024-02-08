# def solution(arr):
#     answer = []
#     for x in arr:
#         if x >= 50 and x % 2 == 0:
#             answer.append(x//2)
#         elif x < 50 and x % 2 == 1:
#             answer.append(x*2)
#         else:
#             answer.append(x)
#     return answer

def solution(arr):
    answer = []
    for i in arr:
        if i >= 50 and i % 2 == 0:
            answer.append(i//2)
        elif i < 50 and i % 2 == 1:
            answer.append(i*2)
        else:
            answer.append(i)
    return answer
                        