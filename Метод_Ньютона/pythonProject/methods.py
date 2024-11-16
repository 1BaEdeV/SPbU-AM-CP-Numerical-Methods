import math

def brude_force(func, a,b):
    n=1
    x=a
    while True:
        if x==b:
            x=a
            n/=2
        xk=x+n
        if func(xk)*func(xk) < 0:
            return x,xk
        if func(xk)*func(xk) == 0:
            if func(x) == 0:
                return x,x
            if func(xk) == 0:
                return xk,xk
        x=xk
def resh_search(func,dfunc,a,b,eps=10**-5):
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
        c = func(xk)
        if c<0:
            ak=c
        if c>=0:
            bk=c
        if abs(xk-x) < eps:
            return xk
        print(xk)
        x=xk
def func(a):
    return a+5
def dfunc(a):
    return 1
print(resh_search(func,dfunc, -10,10))
ч



