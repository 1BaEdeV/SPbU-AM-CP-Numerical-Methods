from math import cos
import numpy as np

def f(x):
    return x**3 - np.exp(x) + 1
# Узлы (равномерные и Оптимальные)
def Nuzl(a, b, n):
    return [a + i * (b - a) / (n-1) for i in range(n)]

def Optuzl(a, b, n):
    return [0.5 * ((b - a) * cos((2 * i + 1) * np.pi / (2 * n + 2)) + (b + a)) for i in range(n + 1)]

def max_deviation(f, ipf):
    return max(abs(f[i]-ipf[i]) for i in range(len(ipf)))

def absolute_error(true_values, approx_values):
    errors = [abs(true_values[i] - approx_values[i]) for i in range(len(true_values))]
    return errors
