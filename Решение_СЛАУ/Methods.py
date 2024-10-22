import class_matrix as Matrix

def MoSI(A,b, eps=1e-13):
    nu = 1 / A.normainf()
    B = A.E() - A * nu
    Bnorm = B.normainf()
    if Bnorm >= 1:
        T = ~A
        A , b = T*A, T*b
        nu = 1/A.normainf()
        B = A.E() - A * nu
        Bnorm = B.normainf()
    c=nu*b
    xk=c
    print(Bnorm)
    while True:
        xk1 = B * xk + c
        if (Bnorm/(1-Bnorm))*(xk1-xk).vecnorma()<eps and Bnorm<1:
            return xk1
        elif Bnorm>=1 and (A*xk1-b).vecnorma()<eps:
            return xk1
        """Здесь уже в транспонированную матрицу просто подставляем наши значения и вычитаем вектор b, потому что как по-другому проверить я уж и не знаю"""
        xk=xk1
