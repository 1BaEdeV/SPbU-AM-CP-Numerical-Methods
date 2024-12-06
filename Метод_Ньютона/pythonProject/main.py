import math
from Решение_СЛАУ.Methods import LUP
from Решение_СЛАУ.class_matrix import *
from funcs import *
from methods import *

print('Метод Ньютона')

a,b=-10,10
a1,b1=brudef(func,a,b)
print(a1,b1)
resh=newton(func,dfunc,a,b)
print(f'Решение нелинейного уравнения {resh}')
print(f'Погрешность решения {func(resh)}')
sysresh=sysnewton(sysfunc,dsysfunc,0.000001)

print(f'Решение нелинейного уравнения')
sysresh.PrintM()
print(f'Погрешность решения')
sysfunc(round(sysresh.matrix[0][0],5),round(sysresh.matrix[1][0],5),1).PrintM()


