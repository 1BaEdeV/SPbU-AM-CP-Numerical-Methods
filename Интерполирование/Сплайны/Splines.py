from Решение_СЛАУ import class_matrix
from Решение_СЛАУ import Methods
from ПЛН.funcs import *


def linSply(a,b,n)->list:
    Xargs = Nuzl(a, b, n)
    Yargs = [f(Xargs[i]) for i in range(n)]
    Acoefs=[0]*2*n
    for i in range(n-1):
        X=class_matrix.Matrix([[Xargs[i],1],[Xargs[i+1],1]])
        y=class_matrix.Matrix([Yargs[i],Yargs[i+1]])
        solve=Methods.LUP(X,y)
        Acoefs[2*i],Acoefs[2*i+1]=float(solve.matrix[0][0]), float(solve.matrix[1][0])
    return Acoefs

def LinearSpline(x,Acoefs,Xargs,n):
    for i in range(n):
        if Xargs[i]<=x<=Xargs[i+1]:
            return Acoefs[2*i]*x+Acoefs[2*i+1] # Линейный вид ax+b


def quadrSply(a, b, n) -> list:
    Xargs = Nuzl(a, b, n)
    Yargs = [f(Xargs[i]) for i in range(len(Xargs))]
    Acoefs = [0] * (3 * (n - 1))
    X = []
    Y = []
    for i in range(n - 1):
        for j in range(2):
            mas = [0] * (3 * (n - 1))
            mas[i * 3] = Xargs[i + j] ** 2
            mas[i * 3 + 1] = Xargs[i + j]
            mas[i * 3 + 2] = 1
            X.append(mas)
            Y.append(Yargs[i + j])
        if i < n - 2:
            mas = [0] * (3 * (n - 1))
            mas[i * 3] = 2 * Xargs[i + 1]
            mas[i * 3 + 1] = 1
            mas[(i + 1) * 3] = -2 * Xargs[i + 1]
            mas[(i + 1) * 3 + 1] = -1
            X.append(mas)
            Y.append(0)
    mas = [0] * (3 * (n - 1))
    mas[0] = 2
    X.append(mas)
    Y.append(0)

    X = class_matrix.Matrix(X)
    Y = class_matrix.Matrix(Y)

    solve = Methods.LUP(X, Y)

    for i in range(n - 1):
        Acoefs[3 * i] = float(solve.matrix[3 * i][0])
        Acoefs[3 * i + 1] = float(solve.matrix[3 * i + 1][0])
        Acoefs[3 * i + 2] = float(solve.matrix[3 * i + 2][0])

    return Acoefs


def QuadraticSpline(x,Xargs,Acoefs,n)->list:
    for i in range(n):
        if Xargs[i] <= x <= Xargs[i + 1]:
            return Acoefs[3 * i] * (x ** 2) + Acoefs[3 * i + 1] * x + Acoefs[3 * i + 2]

def cubSply(a,b,n)->list:
    Xargs = Nuzl(a, b, n)
    Yargs = [f(x) for x in Xargs]
    h=[Xargs[i+1]-Xargs[i] for i in range(n-1)]
    hy=[Yargs[i+1]-Yargs[i] for i in range(n-1)]
    gamma=[6*((Yargs[i+1]-Yargs[i])/h[i] - (Yargs[i]-Yargs[i-1])/h[i-1]) for i in range(1,n-1)]
    H=[]
    for i in range(n-2):
        mas = [0] * (n - 2)
        if i == 0:
            mas[i] = 2 * (h[i] + h[i + 1])
            mas[i + 1] = h[i + 1]
        elif i == n - 3:
            mas[i - 1] = h[i]
            mas[i] = 2 * (h[i] + h[i + 1])
        else:
            mas[i - 1] = h[i]
            mas[i] = 2 * (h[i] + h[i + 1])
            mas[i + 1] = h[i + 1]
        H.append(mas)
    matrdif2y=Methods.LUP(class_matrix.Matrix(H),class_matrix.Matrix(gamma))
    dif2y=[float(matrdif2y.matrix[i][0]) for i in range(n-2)]
    dif2y = [0] + dif2y + [0]
    diff1=[float(hy[i]/h[i]-dif2y[i+1]*h[i]/6-dif2y[i]*h[i]/3) for i in range(n-1)]
    coefs=[0]*(4*(n-1))
    for i in range(n - 1):
        coefs[4 * i] = float(Yargs[i])
        coefs[4 * i + 1] = diff1[i]
        coefs[4 * i + 2] = dif2y[i] / 2
        coefs[4 * i + 3] = (dif2y[i + 1] - dif2y[i]) / (6 * h[i])
    return coefs


def CubicSpline(x, Xargs, coefs,n) -> float:
    for i in range(n-1):
        if Xargs[i] <= x <= Xargs[i + 1]:
            return coefs[4*i] + coefs[4*i + 1]*(x-Xargs[i])+coefs[4*i + 2]*(x-Xargs[i])**2+coefs[i*4 + 3]*(x-Xargs[i])**3
    return None