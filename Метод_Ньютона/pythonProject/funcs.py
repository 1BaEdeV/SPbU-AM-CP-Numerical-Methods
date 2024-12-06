from math import *
from Решение_СЛАУ.class_matrix import *
def func(x):
    return x**3-exp(x)+1
def dfunc(x):
    return 3*x**2-exp(x)
def sysfunc(x,y,l=1):
    return Matrix([l*sin(y)+2*x-2, y+l*cos(x-1)-0.7])
def dsysfunc(x,y,l=1):
    return Matrix([[2,-l*sin(x-1)],[l*cos(y),1]])