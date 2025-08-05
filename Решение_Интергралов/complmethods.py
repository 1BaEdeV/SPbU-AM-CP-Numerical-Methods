import numpy as np
from numpy.linalg import solve
import matplotlib.pyplot as plt


def cardano(A):
    a,b,c,d=A[0],A[1],A[2],A[3]
    q=(2*b**3/(27*a**3)-b*c/(3*a**2)+d/a)/2
    p=(3*a*c-b**2)/(9*a**2)
    r=np.sign(q)*np.sqrt(np.abs(p))
    phi=np.arccos(q/r**3)

    y=np.array([-2*r*np.cos(phi/3),
                2*r*np.cos(np.pi/3-phi/3),
                2*r*np.cos(np.pi/3+phi/3)])
    x=y-b/(3*a)
    return x


def moment(a,b,al,be,i):
    coef=max(al,be)
    return (b**(i-coef+1)-a**(i-coef+1))/(i-coef+1)


def gauss(f,a,b,al,bet,parts=100):
    if al==0:
        t,f_=b, lambda x: f(t-x)
    else:
        t,f_=a, lambda x: f(x+t)
    a,b=0,b-a
    res=0
    #Количество узлов для метода
    n=3

    for i in range(parts):
        lb = a + i * (b - a) / parts
        rb = a + (i + 1) * (b - a) / parts

        #1. Вычисляем моменты
        moments=np.array([moment(lb,rb,al,bet,i) for i in range(2*n)])

        #2. СЛАУ для коефов a
        mu_matrix=np.zeros((n,n))
        for i in range(n):
            for j in range(n):
                mu_matrix[i,j]=moments[i+j]
        mu_vector = moments[n:]
        a_coef=solve(mu_matrix,-mu_vector)
        poly=np.append([1],a_coef[::-1])
        #3. Поиск узлов как корней узлового многочлена
        xj=cardano(poly)

        #4. СЛАУ для коефов A
        x_matrix=np.array([xj ** s for s in range(n)])
        mu_vector = moments[:n]
        A=solve(x_matrix,mu_vector)
        for i in range(n):
            res+=f_(xj[i])*A[i]
    return res


def newton_cotes(f,a,b,al,bet,parts=100):
    if al == 0:
        t, f_ = b, lambda x: f(t - x)
    else:
        t, f_ = a, lambda x: f(x + t)
    a, b = 0, b - a

    res = 0

    # Количество узлов для метода
    n = 3

    for i in range(parts):
        nodes=np.array([a+(b-a)*i/parts,
                        a+(b-a)*(i+1/2)/parts,
                        a+(b-a)*(i+1)/parts])
        #1. Вычисляем моменты
        mu_vector = np.array([moment(nodes[0],nodes[2],al,bet,i) for i in range(n)])
        nodes_matrix=np.zeros((n,n))
        for i in range(n):
            for j in range(n):
                nodes_matrix[i,j]=nodes[j]**i
        A=solve(nodes_matrix,mu_vector[:n])
        for i in range(n):
            res+=A[i]*f_(nodes[i])
    return res