import math
from Решение_СЛАУ.Methods import LUP
from Решение_СЛАУ.class_matrix import *
from funcs import *
def brudef(func, a,b):
    n=1
    x=a
    while True:
        if x==b:
            x=a
            n/=2
        xk=x+n
        print(xk, x)
        if func(xk)*func(xk) < 0:
            return x,xk
        if func(xk)*func(xk) == 0:
            if func(x) == 0:
                return x,x
            if func(xk) == 0:
                return xk,xk
        x=xk
def newton(func,dfunc,a,b,eps=10**-5):
    """Метод хорд"""
    ak=a
    bk=b
    x=a
    while True:
        if dfunc(x) == 0:
            if x==a:
                x+=eps
            else:
                x-=eps
        xk=x-func(x)/dfunc(x)
        if not(ak<=xk<=bk):
            xk = (ak+bk)/2
        if func(a)*func(xk) < 0:
            bk=xk
        else:
            ak=xk
        if abs(xk-x) < eps:
            return xk
        x=xk

def sysbrudef(sysfunc, dsysfunc):
    n=10
    values=Matrix([0,0])
    i=0
    while i<=n:
        delta=LUP(dsysfunc(values.matrix[0][0],values.matrix[1][0],i/n),-1*sysfunc(values.matrix[0][0],values.matrix[1][0],i/n))
        values+=delta
        i+=1
    return values



def sysnewton(sysfunc, dsysfunc,eps=10**-4):
    values = sysbrudef(sysfunc, dsysfunc)
    print("Начальное приблежение")
    values.PrintM()
    print("")
    while True:
        delta=delta=LUP(dsysfunc(values.matrix[0][0],values.matrix[1][0]),-1*sysfunc(values.matrix[0][0],values.matrix[1][0]))
        values_=delta+values
        if (values_-values).vecnorma() < eps:
            return values_
        values=values_







