import random
def randInt(min=0,max=0):
    if(max == 50):
        return random.random() * 50
    elif min==50:
        return (random.random() * 50)*2
    elif min==50 and max==500:
        return (random.random() * 50)*10
    else:
        return random.random() * 100

print(randInt(50,500))