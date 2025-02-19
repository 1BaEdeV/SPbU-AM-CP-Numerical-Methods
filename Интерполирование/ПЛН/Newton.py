from ПЛН.funcs import *

def divided_differences(n, mas):
    coef = [f(mas[i]) for i in range(n)]
    for j in range(1, n):
        for i in range(n-1, j - 1, -1):
            coef[i] = (coef[i] - coef[i - 1]) / (mas[i] - mas[i - j])
    return coef

def Nn(x, a, b, n):
    xmas = Nuzl(a, b, n)
    coef = divided_differences(n, xmas)
    p = coef[n-1]
    for k in range(n-2, -1, -1):
        p = p * (x - xmas[k]) + coef[k]
    return p

def Noptn(x, a, b, n):
    xmas = Optuzl(a, b, n)
    coef = divided_differences(n, xmas)
    p = coef[n-1]
    for k in range(n-2, -1, -1):
        p = p * (x - xmas[k]) + coef[k]
    return p
