import Решение_СЛАУ.class_matrix as Matrix

def MoSI(A,b, eps=10**-7):
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
    xk=c.copy()
    k=0
    while True:
        xk1 = B * xk + c
        if (Bnorm/(1-Bnorm))*(xk1-xk).vecnorma()<eps and Bnorm<1:
            return xk1,k
        elif Bnorm>=1 and (A*xk1-b).vecnorma()<eps:
            return xk1,k
        """Здесь уже в транспонированную матрицу просто подставляем наши значения и вычитаем вектор b, потому что как по-другому проверить я уж и не знаю"""
        xk=xk1
        k+=1
def Seidel(A,b, eps=1e-3):
    C=[]
    if  A.diagpre()==False:
        T=~A
        A,b=T*A,T*b
    d = b.copy()
    for i in range(len(A.matrix)):
        res = []
        for j in range(len(A.matrix)):
            if i == j:
                res.append(0)
            else:
                res.append(-A.matrix[i][j] / A.matrix[i][i])
        d.matrix[i][0] /= A.matrix[i][i]
        C.append(res)
    k=0
    xk1=d.copy()
    while True:
        for i in range(len(C)):
            sum = 0
            for j in range(len(C)):
                sum += C[i][j] * xk1.matrix[j][0]
            xk1.matrix[i][0] = sum + d.matrix[i][0]

        if (A * xk1 - b).vecnorma() < eps:
            return xk1, k
        k += 1
def LUP(A,b):
    n=len(A.matrix)
    E=A.E()
    M=A.copy()
    P=E.copy()
    "Преобразовываем матрицу исходную и матрицу перестановок"
    for i in range(n-1):
        k=i
        for j in range(i,n):
            if abs(M.matrix[i][k])<abs(M.matrix[j][i]):
                k=j
        c=M.getitem("raw",k)
        t=M.getitem("raw",i)
        M.matrix[k],M.matrix[i]=t,c
        c = P.getitem("raw", k)
        t = P.getitem("raw", i)
        P.matrix[k], P.matrix[i] = t, c
        "Преобразовываем элементы матрицы M"
        for l in range(i+1,n):
            M.matrix[l][i]=M.matrix[l][i]/ M.matrix[i][i]
            for m in range(i+1,n):
                M.matrix[l][m]=M.matrix[l][m]-M.matrix[l][i]*M.matrix[i][m]

    "Раскладываем M на матрицы L и U"
    L=E.copy()
    U=E.copy()
    for i in range(n):
        for j in range(n):
            if i==j:
                L.matrix[i][j]=1
                U.matrix[i][j]=M.matrix[i][j]
            if j>i:
                U.matrix[i][j]=M.matrix[i][j]
            if i>j:
                U.matrix[i][j]=0
                L.matrix[i][j]=M.matrix[i][j]
    "Решаем систему Ly=Pb Ux=y"
    Pb=P*b
    y=Matrix.Matrix([0 for i in range(len(A.matrix))])
    "Вычисляем Ly=Pb"
    for k in range(n):
        y.matrix[k][0]=Pb.matrix[k][0]
        for i in range(k):
            y.matrix[k][0]-=L.matrix[k][i]*y.matrix[i][0]
    "Обратным ходом по матрице вычисляем Ux=y"
    x=Matrix.Matrix([0 for i in range(len(A.matrix))])
    for i in reversed(range(n)):
        x.matrix[i][0]=y.matrix[i][0]/U.matrix[i][i]
        for j in range(i+1,n):
            x.matrix[i][0]-=U.matrix[i][j]*x.matrix[j][0]/U.matrix[i][i]
    return x


def QR(A,b):
    n = len(A.matrix)
    E=A.E()
    Q=A.E()
    R=A.copy()
    for i in range(n-1):
        y=Matrix.Matrix([R.matrix[j][i] for j in range(i,n)])
        z=Matrix.Matrix([E.matrix[i][k] for k in range(i,n)])
        alp=y.vecnorma()
        ro=(y-alp*z).vecnorma()
        w=(y-alp*z)/ro
        Qprom = E.copy()
        Qprom_ = w.E() - 2 * w * ~w
        for j in range(i, n):  # Вкладываем матрицу размерности n-номер итерации в единичную матрицу исходного размера
            for k in range(i, n):
                Qprom.matrix[j][k] = Qprom_.matrix[j - i][k - i]
        Q = Q * ~Qprom
        R = Qprom * R
    """QRx=b и Rx=QTb"""
    y=~Q*b
    x = Matrix.Matrix([0 for i in range(len(A.matrix))])
    for i in reversed(range(n)):
        x.matrix[i][0] = y.matrix[i][0] / R.matrix[i][i]
        for j in range(i + 1, n):
            x.matrix[i][0] -= R.matrix[i][j] * x.matrix[j][0] / R.matrix[i][i]
    return x











