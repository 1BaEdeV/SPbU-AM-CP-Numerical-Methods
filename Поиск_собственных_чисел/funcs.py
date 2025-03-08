import random
from Решение_СЛАУ import class_matrix
import numpy as np
from Решение_СЛАУ.class_matrix import Matrix
import math

def randdig(n, min_val=0, max_val=10):
    return [[random.randint(min_val, max_val) if i == j else 0 for j in range(n)] for i in range(n)]

def randmatr(n, min_val=0, max_val=10):
    matrix = [[random.randint(min_val, max_val) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matrix[i][i] += n  # Усиливаем диагональ
    return matrix
def randvec(n, min_val=0, max_val=5):
    return [random.randint(min_val, max_val) for j in range(n)]

def hessenberg(A: class_matrix.Matrix):
    n = A.dim()[0]
    Hess = A.copy()
    for i in range(n - 2):
        H=A.E(n)
        w=Matrix([0]*(n))
        for j in range(i+1, n):
            w.matrix[j - i][0]=A.matrix[j][0]
        norm =(-1 if w.matrix[1][0] >= 0 else 1)* math.sqrt(sum([w.matrix[j][0]**2 for j in range(1, n - i)]))
        if norm != 0:
            H=A.E(n)
            nu = 1 / math.sqrt((2 * norm * (norm - w.matrix[1][0])))
            w.matrix[1][0]-=norm
            w = w*nu
            block = A.E(n) - 2 * (w * ~w)
            for j in range(i, n):
                for k in range(i, n):
                    H.matrix[j][k] = block.matrix[j][k]
        Hess = H * Hess * H
        return Hess


def eigQR(A):
    n = A.dim()[0]
    E = A.E(n)
    R = A.copy()
    Q = E.copy()
    for i in range(n - 1):
        G = A.E(n).copy()
        if abs(R.matrix[i + 1][i]) > 0.0000000001:
            t = R.matrix[i][i] / R.matrix[i + 1][i]
            c = 1 / math.sqrt(1 + t ** 2)
            s = t * c
        else:
            c, s = 0, 1
        G.matrix[i][i], G.matrix[i + 1][i + 1], G.matrix[i][i + 1], G.matrix[i + 1][i] = s, s, c, -c
        Q = Q * ~G
        R = G * R
    return Q, R

A=class_matrix.Matrix([[5,-3,-1],[-5,2.08,0.56],[0,-0.44,-1.08]])
c=eigQR(A)



"""
"""
"""
n = len(A.matrix)
    E=A.E(n)
    Q=E.copy()
    R=A.copy()
    for i in range(n-1):
        y=class_matrix.Matrix([R.matrix[j][i] for j in range(i,n)])
        z=class_matrix.Matrix([E.matrix[i][k] for k in range(i,n)])
        alp=y.vecnorma()
        ro=(y-alp*z).vecnorma()
        w=(y-alp*z)/ro
        Qprom = E.copy()
        Qprom_ = w.E(n-i) - 2 * w * ~w
        for j in range(i, n):  # Вкладываем матрицу размерности n-номер итерации в единичную матрицу исходного размера
            for k in range(i, n):
                Qprom.matrix[j][k] = Qprom_.matrix[j - i][k - i]
        Q = Q * ~Qprom
        R = Qprom * R
    return Q, R"""