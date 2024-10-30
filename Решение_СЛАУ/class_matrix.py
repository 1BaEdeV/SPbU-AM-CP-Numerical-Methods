import math

import funcs
class Matrix:
    def __init__(self, matr=[]):
        if  not funcs.is_2d_array(matr):
            result=[]
            for i in range(len(matr)):
                res=[]
                for j in range(len(matr)):
                    if j==0:
                        res.append(matr[i])
                    else:
                        res.append(0)
                result.append(res)
            self.matrix=result
        else:
            self.matrix=matr

    def dim(self):
        """Возвращает размерность матрицы в виде (n, m) - tuple.
        Если это вектор, корректно обрабатывает его."""

        rows = len(self.matrix)  # Количество строк

        # Проверка на вектор-строку или вектор-столбец
        if rows == 0:
            return (0, 0)  # Пустая матрица
        if isinstance(self.matrix[0], list):
            cols = len(self.matrix[0]) if rows > 0 else 0  # Количество столбцов в первой строке
        else:
            cols = 1  # Если первый элемент — не список, значит это вектор-столбец

        return rows, cols
    def add_row(self, row):
        """Добавление строки в матрицу"""
        self.matrix.append(row)
        return self
    def add_col(self, col):
        """Добавление столбуа в матрицу"""
        for i in range(len(self.matrix)):
            self.matrix[i].append(col[i])
        return self
    def add_matrix(self, matrix):
        """Добавление матрицы в пустой объект"""
        for i in range(len(matrix)):
            self.matrix.append(matrix[i])
        return self

    def PrintM(self):
        """Вывод матрицы с выравниванием, включая случай с вектором, с поддержкой float и int"""
        if funcs.is_vector(self.matrix):
            # Выводим только первый столбец
            for row in self.matrix:
                print("".join(f"{row[0]:7.15f}" if isinstance(row[0], float) else f"{row[0]:3}"))
        else:
            # Обычный вывод матрицы с поддержкой как float, так и int
            for row in self.matrix:
                print(" ".join(f"{num:7.15f}" if isinstance(num, float) else f"{num:3}" for num in row))

    def getitem(self, type, idx=0):
        """Возвращает строку/столбец/элемент матрицы, raw-строка, сlm-столбец, elm-элемент"""
        if type == "raw":
            return self.matrix[idx]
        if type == "clm":
            result = []
            for i in range(len(self.matrix)):
                result.append(self.matrix[i][idx])
            return result
        if type == "dig":
            result = []
            for i in range(len(self.matrix)):
                result.append(self.matrix[i][i])
            return result
        if type == "elm":
            return self.matrix[idx[0]][idx[1]]

    def __eq__(self, other):
        """A==B - возвращает T/F"""
        return self.matrix == other.matrix
    def __ne__(self, other):
        """A!=B - возвращает T/F"""
        return self.matrix != other.matrix
    def __add__(self, other):
        """Сложение 2 матриц/векторов"""
        result = []
        row, col = self.dim()
        rowother, colother = self.dim()
        if colother == 1 and col == 1:
            for i in range(len(self.matrix)):
                result.append(self.matrix[i]+other.matrix[i])
            return Matrix(result)
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[i])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)
        return Matrix(result)


        return Matrix(result)
    def __sub__(self, other):
        """Разность 2 матриц"""
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[i])):
                row.append(self.matrix[i][j] - other.matrix[i][j])
            result.append(row)
        return Matrix(result)
    def __truediv__(self, other):
        matrix = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix)):
                elem = self.matrix[i][j] / other
                row.append(elem)
            matrix.append(row)
        return Matrix(matrix)

    def __mul__(self, other):
        """Умножение матрицы или вектора на скаляр или на матрицу этого же рзмера"""
        result = []
        if isinstance(other, float) or isinstance(other, int):
            matrix = []
            for i in range(len(self.matrix)):
                row = []
                for j in range(len(self.matrix)):
                    elem = self.matrix[i][j] * other
                    row.append(elem)
                matrix.append(row)
            return Matrix(matrix)
        else:
            matrix = []
            for i in range(len(self.matrix)):
                row = []
                for j in range(len(self.matrix)):
                    elem = 0
                    for k in range(len(self.matrix)):
                        elem += self.matrix[i][k] * other.matrix[k][j]
                    row.append(elem)
                matrix.append(row)

            return Matrix(matrix)

    def __rmul__(self, other):
        """Функция позволяет коммутативно умножать матрицу на число"""
        return self * other
    def __invert__(self):
        result = []
        for i in range(len(self.matrix)):
            res = []
            for j in range(len(self.matrix[i])):
                res.append(self.matrix[j][i])
            result.append(res)
        return Matrix(result)
    def E(self):
        "Единичная матрица размерности этой"
        result = []
        for i in range(len(self.matrix)):
            res = []
            for j in range(len(self.matrix[i])):
                if i == j:
                    res.append(1)
                else:
                    res.append(0)
            result.append(res)
        return Matrix(result)
    def norma1(self):
        """Вычисление единичной нормы матрицы(максимальная из сумм элементво по столбцам)"""
        res=[]
        for i in range(len(self.matrix)):
            clm = self.getitem("clm", i)
            res.append(sum(abs(clm[j]) for j in range(len(clm))))
        return max(res)
    def normainf(self):
        """Вычисление бесконечномерной нормы матрицы(максимальная из сумм элементво по столбцам)"""
        res = []
        for i in range(len(self.matrix)):
            res.append(sum(abs(self.matrix[i][j]) for j in range(len(self.matrix[i]))))
        return max(res)

    def vecnorma(self):
        """Евклидова норма вектора"""
        res = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                res+=(self.matrix[i][j])**2
        return math.sqrt(res)

    def diagpre(self):
        for i in range(len(self.matrix)):
            if 2*self.matrix[i][i]-sum(self.matrix[i])<0:
                return False
        return True
    def copy(self):
        matr=[]
        for i in range(len(self.matrix)):
            res=[]
            for j in range(len(self.matrix)):
                res.append(self.matrix[i][j])
            matr.append(res)
        return Matrix(matr)

    def swap(self,str,a,b):
        if str =="raw":
            for i in range(len(self.matrix)):
                self.matrix[a][i],self.matrix[b][i]=self.matrix[b][i],self.matrix[a][i]
        if str == "col":
            for i in range(len(self.matrix)):
                self.matrix[i][a],self.matrix[i][b]=self.matrix[i][b],self.matrix[i][a]
