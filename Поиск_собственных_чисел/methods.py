from Решение_СЛАУ import class_matrix
from Решение_СЛАУ.Methods import *
from funcs import *

def PM(A: class_matrix.Matrix):
    n=A.dim()[0]
    delta, rtol = 10 ** -8, 10 ** -6
    y=class_matrix.Matrix([1]*n)
    z=y/y.vecnorma()
    lambd=class_matrix.Matrix([0]*n)
    while True:
        counterI=0
        ilambd=class_matrix.Matrix([0]*n)
        y=A*z

        for i in range(n):
            if abs(z.matrix[0][i])>delta:
                ilambd.matrix[0][i]=y.matrix[0][i]/z.matrix[0][i]
                counterI+=1

        z = y / y.vecnorma()

        if (ilambd-lambd).normainf()<=rtol*max(ilambd.normainf(),lambd.normainf()):
            ans=sum(lambd.matrix[0])/counterI
            return ans,z.matrix[0]

        lambd=ilambd.copy()

def invPM(A: class_matrix.Matrix, sigma):
    n=A.dim()[0]
    delta, rtol = 10 ** -8, 10 ** -10
    y=class_matrix.Matrix([1]*n)
    z=y/y.vecnorma()
    while True:
        counterI=0
        ilambd=class_matrix.Matrix([0]*n)
        y=LUP(A-sigma*A.E(n),z)
        for i in range(n):
            if abs(y.matrix[0][i])>delta:
                ilambd.matrix[0][i]=z.matrix[0][i]/y.matrix[0][i]
                counterI+=1
        z = y / y.vecnorma()
        if counterI!=0:
            ans = sigma + sum([ilambd.matrix[0][i] for i in range(n)]) / counterI

            if abs(sigma-ans)<=rtol:
                return ans,[z.matrix[0][i] for i in range(n)]
            sigma=ans
        else:
            raise ValueError("Ошибка: Деление на ноль в invPM (counterI = 0)")

def QRalg(A: class_matrix.Matrix):
    eps=10**-10
    n=A.dim()[0]
    E=A.E(n)
    H=hessenberg(A)
    eigs=[]
    prev_bnn=None
    while True:
        bn=H.matrix[-1][-1]
        Q,R=eigQR(H-bn*E)
        H=R*Q+bn*E
        if prev_bnn is not None and abs(H.matrix[-1][-1] - prev_bnn) < (1 / 3) * abs(prev_bnn):
            if abs(H.matrix[-1][-2])<eps:
                if n>2:
                    eigs.append(H.matrix[-1][-1])
                    H=class_matrix.Matrix([[H.matrix[k][j] for k in range(n-1)]for j in range(n-1)])
                    n-=1
                    E=H.E(n)
                if n==2:
                    eigs.append(H.matrix[0][0])
                    eigs.append(H.matrix[1][1])
                return eigs
        prev_bnn = H.matrix[-1][-1]
        H = hessenberg(H)

