from funcs import *

def basis(x, method, k, n, a=-2, b=5):
    mas = Nuzl(a, b, n) if method == 1 else Optuzl(a, b, n)
    basis = 1
    for j in range(n):
        if j != k:
            basis*=(x-mas[j])/(mas[k]-mas[j])
    return basis*f(mas[k])
def Ln(x, a, b, n):
    return sum(basis(x,1, i, n,a,b) for i in range(n))

def Loptn(x,a,b, n):
    return sum(basis(x, 0, i, n,a,b) for i in range(n))
