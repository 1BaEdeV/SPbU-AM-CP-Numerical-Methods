class Matdata:
    def __init__(self,a,b):
        self.A = a
        self.b = b

test0 = Matdata(
    [[0,2,3],
        [1,2,3],
        [2,3,4]],

    [13,17,32]
)

N = 1

test1 = Matdata(
  [[N+2, 1, 1],
      [1, N+4, 1],
      [1, 1, N+6]],

    [N+4, N+6, N+8]
)
test2 = Matdata(
  [[-(N+2), 1, 1],
     [1, -(N+4), 1],
     [1, 1, -(N+6)]],

  [-(N+4), -(N+6), -(N+8)]
)

test3 = Matdata(
    [[-(N + 2), N+3, N+4],
     [N+5, -(N + 4), N+1],
     [N+4, N+5, -(N + 6)]],

    [N + 4, N + 6, N + 8]
)

test4 = Matdata(
    [[N + 2, N+1, N+1],
     [N+1, N + 4, N+1],
     [N+1, N+1, N + 6]],

    [N + 4, N + 6, N + 8]
)
n = 3
e=10^-4
masA=[]
masb=[]
prom=[]
for i in range(n):
    for j in range(n):
        if i==j:
            prom.append(1)
        if i<j:
            prom.append(-1)
        else:
            prom.append(0)
        masb.append(-1)
        if j==n-1:
            masb.append(1)
    masA.append(prom)

test5 = Matdata(masA,masb)








