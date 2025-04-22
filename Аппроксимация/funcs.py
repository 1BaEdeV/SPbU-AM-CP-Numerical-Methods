import math
import random

def func(x):
    return x**3-math.sin(x)
def Randuzl(a, b, m):
    return [a+(b - a)*random.random() for i in range(m)]

def values_generator(args: list[float]) -> list[float]:
    vals = [func(arg) for arg in args]
    data_set = []
    for val in vals:
        data_set.append(val + (random.random() - 0.5) / 5)#Погрешность от 0 до 0.1
    return data_set

def Nuzl(a, b, n):
    return [a + i * (b - a) / (n-1) for i in range(n)]

def lost(values, calculated_values):
    loss = sum((values[i] - calculated_values[i]) ** 2 for i in range(len(values)))
    return loss


