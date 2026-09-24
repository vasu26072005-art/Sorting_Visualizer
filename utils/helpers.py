# Code for generating Random Array
import random

def generateArray(numberOfBars, minValue, maxValue):
    arr = []

    for _ in range(numberOfBars):
        val = random.randint(minValue, maxValue)
        arr.append(val)

    return arr    