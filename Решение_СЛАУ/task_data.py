class Matdata:
    def __init__(self,a,b):
        self.A = a
        self.b = b

N = 2.

def testdata(n):
    if n == 0:
        data = Matdata(
            [[0.,2.,3.],
                [1.,2.,4.],
                [4.,5.,6.]],

            [13.,17.,32.]
        )
        return data

    if n ==1:
        data = Matdata(
          [[N+2., 1., 1.],
              [1., N+4., 1.],
              [1., 1., N+6.]],

            [N+4., N+6., N+8.]
        )
        return data
    if n == 2:
        data = Matdata(
          [[-(N+2.), 1., 1.],
             [1., -(N+4.), 1.],
             [1., 1., -(N+6.)]],

          [-(N+4.), -(N+6.), -(N+8.)]
        )
        return data
    if n == 3:
        data = Matdata(
            [[-(N + 2.), N+3., N+4.],
             [N+5., -(N + 4.), N+1.],
             [N+4., N+5., -(N + 6.)]],

            [N + 4., N + 6., N + 8.]
        )
        return data
    if n == 4:
        data = Matdata(
            [[N + 2., N+1., N+1.],
             [N+1., N + 4., N+1.],
             [N+1., N+1., N + 6.]],

            [N + 4., N + 6., N + 8.]
        )
        return data

def test5(n,eps=10**-4):
    masA=[]
    masb=[]
    prom=[]
    for i in range(n):
        prom=[]
        for j in range(n):
            if i==j:
                prom.append(1+eps*N)
            if i<j:
                prom.append(-1-eps*N)
            if j<i:
                prom.append(eps*N)
        if i==n-1:
            masb.append(1)
        else:masb.append(-1)
        masA.append(prom)
    return Matdata(masA,masb)

print(test5(4,0.001).A)