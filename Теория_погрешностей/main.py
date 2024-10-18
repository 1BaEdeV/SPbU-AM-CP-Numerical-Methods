from prettytable import PrettyTable
import math


eps=0.000001
"""Заданная погрешность"""
eps_sin = (0.000001)/(3*1.86)
""" Вычисленная погрешность синуса"""
eps_arctan = (0.000001) / (3 * 0.422)
""" Вычисленная погрешность арктангенса"""
eps_sqrtt = (0.000001) / 3
"""Вычисленная методическая погрешность(корня грубо говоря)"""


def sin(x):
    """Разложение синуса в ряд Тейлора"""
    val = 0
    n = 0
    while True:
        val_ = val + (-1) ** n * x ** (2 * n+1) / math.factorial(2*n+1)
        if abs(val_ - val) < eps_sin:
            return val_
        val = val_
        n += 1

def arctan(x):
    """Разложение арктангенса в раяд Тейлора """
    n = 0
    if abs(x)<1:
        val = 0
        while True:
            val_ = val + (-1) ** n * x ** (2 * n + 1) / (2 * n + 1)
            if abs(val_ - val) < eps_arctan:
                return val_
            val = val_
            n += 1
    if abs(x)>=1:
        val = math.pi/2 * (x/abs(x))
        while True:
            val_ = val - (-1) ** n * x ** -(2 * n + 1) / (2 * n + 1)
            if abs(val_ - val) < eps_sqrtt:
                return val_
            val = val_
            n += 1

def sqrtt(x):
    """ Разложение корня по формуле Герона """
    eps = (0.000001) / 3
    val = 1
    n = 0
    while True:
        val_ = 0.5*(val+x/val)
        if abs(val_ - val) < eps:
            return val_
        val = val_
        n += 1
    return 0
def insertTOtable(a,c,b):
    x=a
    while x+c<=b:
        mas=[]
        x+=c
        x=round(x,3)
        phi = 1 + arctan(6.4 * x + 1.1)
        phi_= 1 + math.atan(6.4 * x + 1.1)
        psi = sin(2 * x + 1.05)
        psi_ = math.sin(2 * x + 1.05)
        f = sqrtt(phi) / psi
        f_ = math.sqrt(phi) / psi
        z = f
        z_ = math.sqrt(phi_) / psi_
        mas.append(x)
        mas.append(phi)
        mas.append(eps_arctan)
        mas.append(phi_)
        mas.append(abs(phi_-phi))
        mas.append(psi)
        mas.append(eps_sin)
        mas.append(psi_)
        mas.append(abs(psi_ - psi))
        mas.append(f)
        mas.append(eps_sqrtt)
        mas.append(f_)
        mas.append(abs(f_-f))
        mas.append(z)
        mas.append(eps)
        mas.append(z_)
        mas.append(abs(z_ - z))
        MAS.append(mas)

"Итоговые значения"
x=PrettyTable()

"""
d - delta 
bi - built-in function
"""

columns = ["x", "phi(x)", "d_phi", "bi_phi(x)", "bi_d_phi",
           "psi(x)", "d_psi", "bi_psi(x)", "bi_d_psi",
            "f(x)", "d_f", "bi_f(x)", "bi_d_f",
           "z(x)", "d_z", "bi_z(x)", "bi_d_z"]
x.field_names = columns
MAS = []
insertTOtable(0.01,0.005,0.06)
for exp in MAS:
    x.add_row(exp)
print(x)