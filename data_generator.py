import random

def randomSubset(size=25, jump=1):
    result=[]
    for i in range(0, size+1, jump):
        res=random.sample(range(i),i)
        result.append(res)
    return result

