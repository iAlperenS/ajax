from string import *
import random

def rand(num):
    a = ""
    newL = ascii_letters + "1234567890"
    for _ in range(num):
        e = random.choice(newL)
        a += e
    return a