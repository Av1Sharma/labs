import random

def rollem(first, last):
    num1 = random.randint(first, last)
    num2 = random.randint(first, last)
    roll = num1 + num2
    return roll
    
