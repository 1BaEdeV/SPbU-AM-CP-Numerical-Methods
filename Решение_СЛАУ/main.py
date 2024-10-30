import class_matrix
import funcs
from task_data import *
from Methods import *
import numpy
def main():
    eps = 10 ** -5
    for i in range (5):

        A = class_matrix.Matrix(testdata(i).A)
        b = class_matrix.Matrix(testdata(i).b)
        print(f'{"|"*20}Тест {i}{"|"*1000}')

        print("Точное решение")
        M1 = numpy.array(A.matrix)
        v1 = numpy.array(b.getitem("clm",0))
        arr = numpy.linalg.solve(M1,v1)
        arr=arr.tolist()
        print(arr)
        res,n = MoSI(A, b, 10**-3)
        print("Решение методом простых иетраций")
        res.PrintM()
        print(f'Количество итераций {n}, Заданная п. {eps}, Абсолютная п. {(res-(class_matrix.Matrix(arr))).vecnorma()}')

        print("-" * 50)

        print("Точное решение")
        print(arr)
        res, n = Seidel(A, b)
        print("Решение методом Зейделя")
        res.PrintM()
        print(
            f'Количество итераций {n}, Заданная п. {eps}, Абсолютная п. {res.vecnorma() - (class_matrix.Matrix(arr)).vecnorma()}')

        print("-" * 50)

        print("Точное решение")
        print(arr)
        res= LUP(A, b)
        print("Решение методом LU разложения")
        res.PrintM()
        print(f'Заданная п. {eps}, Абсолютная п. {res.vecnorma() - (class_matrix.Matrix(arr)).vecnorma()}')

        print("-" * 50)

        print("Точное решение")
        print(arr)
        res = QR(A, b)
        print("Решение методом QR разложения")
        res.PrintM()
        print(f'Заданная п. {eps}, Абсолютная п. {res.vecnorma() - (class_matrix.Matrix(arr)).vecnorma()}')

    print("")
    print("0" * 10000)
    print("")
    print(f'{"|" * 20}Тест {5}{"|" * 1000}')
    for epss in [10**-3,10**-6]:
        for k in range (4,8):
            A = class_matrix.Matrix(test5(k,epss).A)
            b = class_matrix.Matrix(test5(k,epss).b)
            print("Точное решение")
            M1 = numpy.array(A.matrix)
            v1 = numpy.array(b.getitem("clm", 0))
            arr = numpy.linalg.solve(M1, v1)
            arr = arr.tolist()
            print(arr)
            res, n = MoSI(A, b, 10 ** -3)
            print("Решение методом простых иетраций")
            res.PrintM()
            print(
                f'Количество итераций {n}, Заданная п. {eps}, Заданный размер матрицы {k}, Заданный епсилон{epss}, Абсолютная п. {(res - (class_matrix.Matrix(arr))).vecnorma()}')

            print("-" * 50)

            print("Точное решение")
            print(arr)
            res, n = Seidel(A, b)
            print("Решение методом Зейделя")
            res.PrintM()
            print(f'Количество итераций {n}, Заданная п. {eps}, Заданный размер матрицы {k}, Заданный епсилон{epss}, Абсолютная п. {(res - (class_matrix.Matrix(arr))).vecnorma()}')

            print("-" * 50)

            print("Точное решение")
            print(arr)
            res = LUP(A, b)
            print("Решение методом LU разложения")
            res.PrintM()
            print(f'Количество итераций {n}, Заданная п. {eps}, Заданный размер матрицы {k}, Заданный епсилон{epss}, Абсолютная п. {(res - (class_matrix.Matrix(arr))).vecnorma()}')

            print("-" * 50)

            print("Точное решение")
            print(arr)
            res = QR(A, b)
            print("Решение методом QR разложения")
            res.PrintM()
            print(f'Количество итераций {n}, Заданная п. {eps}, Заданный размер матрицы {k}, Заданный епсилон{epss}, Абсолютная п. {(res - (class_matrix.Matrix(arr))).vecnorma()}')


if __name__ == '__main__':
    main()
