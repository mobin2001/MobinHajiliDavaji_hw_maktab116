from functools import reduce

def multipy(my_list):
    multiply = reduce(lambda x , y: x * y,my_list)
    return multiply

answer = multipy([8,2,3,-1,7])

print(answer)