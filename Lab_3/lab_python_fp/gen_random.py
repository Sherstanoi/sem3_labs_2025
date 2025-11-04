from random import randint
def Gen_random(amount,min,max):
    answer = []
    for i in range(amount):
        answer.append(randint(min,max))
    return answer
# print(Gen_random(100,0,100))
