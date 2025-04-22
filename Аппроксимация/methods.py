import numpy as np
from funcs import *
def basenorm(xvals,fvals,n):
    m=len(xvals)
    E=[]
    for i in range(m):
        mas=[xvals[i]**j for j in range(n+1)]
        E.append(mas)
    E=np.array(E)
    b=np.array(fvals)
    return E.T @ E, E.T @ b

def coefnormMNK(xvals,fvals,n):
    A,b=basenorm(xvals,fvals,n)
    x=np.linalg.solve(A,b)
    ans=[x[i] for i in range(n+1)]
    return ans
def normMNK(vals,coefs):
    n=len(coefs)
    Mas=[]
    for i in range(0,len(vals)):
        Mas.append(sum([(vals[i]**j)*coefs[j] for j in range(n)]))
    return Mas


import numpy as np
import matplotlib.pyplot as plt

def orthogonal_polynomials(x_eval, x_basis, n):
    m = len(x_basis)
    q = np.zeros((n + 1, len(x_eval)))
    qi = np.zeros((n + 1, m))  # значения полиномов на x_basis для расчета коэффициентов
    q[0, :] = 1
    qi[0, :] = 1
    if n > 0:
        q[1, :] = x_eval - np.mean(x_basis)
        qi[1, :] = x_basis - np.mean(x_basis)
    for j in range(1, n):
        alpha = np.sum(x_basis * qi[j] ** 2) / np.sum(qi[j] ** 2)
        beta = np.sum(x_basis * qi[j] * qi[j - 1]) / np.sum(qi[j - 1] ** 2)
        q[j + 1, :] = x_eval * q[j, :] - alpha * q[j, :] - beta * q[j - 1, :]
        qi[j + 1, :] = x_basis * qi[j, :] - alpha * qi[j, :] - beta * qi[j - 1, :]
    return q, qi
def compute_coefficients(y, qi):
    n = len(qi)
    a = np.zeros(n)
    for k in range(n):
        a[k] = np.sum(qi[k] * y) / np.sum(qi[k] ** 2)
    return a
def approximate(x_new, x_basis, y_basis, n):
    q_new, q_basis = orthogonal_polynomials(x_new, x_basis, n)
    a = compute_coefficients(y_basis, q_basis)
    y_approx = np.dot(a, q_new)
    return y_approx


xc=[0,1/4,1/2,3/4,1]
y=[1,2,1,0,1]
x=np.linspace(0,1,100)
q,qi=orthogonal_polynomials(x, xc, 2)
a=coefnormMNK(xc,y,2)
print(a)