import class_matrix
from task_data import *
from Methods import *
import numpy

for i in range (5):
    A=class_matrix.Matrix(testdata(i).A)
    b=class_matrix.Matrix(testdata(i).b)
    print(f'Тест {i}')
    res = MoSI(A, b)
    res.PrintM()

    M1 = numpy.array(A)
    v1 = numpy.array(b)
    arr = numpy.linalg.solve(M1,v1)
    print(arr)